"""factorio.bp.common - common functionality"""

import base64
import collections
import json
import zlib
from typing import Any, TypedDict

type BlueprintType = dict[str, dict[str, Any]]
ItemListType = list[TypedDict("ItemListType", {"name": str, "quality": str, "count": int})]


def count_entities(blueprint: BlueprintType) -> ItemListType:
    """Count all entities in a blueprint

    Args:
        blueprint (BlueprintType): blueprint to enumerate

    Returns:
        list[ItemListType]: list of entities and their number in the blueprint
    """
    items_counter = collections.Counter()
    for entity in blueprint["blueprint"]["entities"]:  # pylint: disable=too-many-nested-blocks
        quality = entity["quality"] if "quality" in entity else "normal"
        items_counter.update(((entity["name"], quality),))
        if "items" in entity:
            for item in entity["items"]:
                module, modules = ("", ""), []
                if ("id" in item) and ("name" in item["id"]):
                    quality = item["id"]["quality"] if "quality" in item["id"] else "normal"
                    module = (item["id"]["name"], quality)
                if ("items" in item) and ("in_inventory" in item["items"]):
                    for in_invent in item["items"]["in_inventory"]:
                        if "stack" in in_invent:
                            modules.append(module)
                items_counter.update(modules)
        if "grid" in entity:
            for grid_item in entity["grid"]:
                if "equipment" in grid_item and "name" in grid_item["equipment"]:
                    quality = grid_item["equipment"]["quality"] if "quality" in grid_item["equipment"] else "normal"
                    items_counter.update(((grid_item["equipment"]["name"], quality),))

    if "tiles" in blueprint["blueprint"]:
        # quality tiles are not really a thing...
        items_counter.update((tile["name"], "normal") for tile in blueprint["blueprint"]["tiles"])

    items = dict(items_counter)
    quality_order = {"normal": 0, "uncommon": 1, "rare": 2, "epic": 3, "legendary": 4}
    return sorted(
        [{"name": name, "quality": quality, "count": count} for (name, quality), count in items.items()],
        key=lambda i: (-i["count"], i["name"], quality_order[i["quality"]]),
    )


def decode(b64_data: str) -> BlueprintType:
    """Decode a blueprint string

    Args:
        b64_data (str): BASE64 encoded blueprint string

    Returns:
        BlueprintType: dict representing the blueprint
    """
    bin_data = base64.b64decode(b64_data[1:])
    json_bin_str = zlib.decompress(bin_data)
    blueprint: BlueprintType = json.loads(json_bin_str)
    return blueprint


def encode(blueprint: BlueprintType, version: int = 0) -> str:
    """Encode a data structure as a blueprint string

    Nothing is checked: if you throw in garbage you will get garbage out.

    Args:
        blueprint (BlueprintType): data structure (dict) for the blueprint
        version (int, optional): version byte, currently always 0

    Returns:
        str: Factorio blueprint string
    """
    json_bin_str = json.dumps(blueprint).encode("utf-8")
    bin_data = zlib.compress(json_bin_str, level=9)
    b64_data = base64.b64encode(bin_data).decode("utf-8")
    return f"{version:d}{b64_data}"
