"""factorio.bp.common - common functionality."""

import base64
import collections
import json
import zlib
from typing import Any, TypedDict

type BlueprintType = dict[str, dict[str, Any]]
ItemListType = list[TypedDict("ItemListType", {"name": str, "quality": str, "count": int})]

QUALITY_ORDER = {"normal": 0, "uncommon": 1, "rare": 2, "epic": 3, "legendary": 4}


def get_value(a_dict: dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Get a value from a dictionary (optionally within another dictionary).

    Args:
        a_dict (dict[str, Any]): main dictionary
        *keys (str): one or more keys, each key is a level lower into the dictionary
        default (Any, optional): optional default

    Returns:
        Any: value found in the dictionary or default / None when not found
    """
    result = a_dict
    for key in keys:
        try:
            result = result[key]
        except KeyError:
            return default
    return result


def count_entities(blueprint: BlueprintType) -> ItemListType:
    """Count all entities in a blueprint.

    Args:
        blueprint (BlueprintType): blueprint to enumerate

    Returns:
        list[ItemListType]: list of entities and their number in the blueprint
    """
    items_counter = collections.Counter()
    for entity in blueprint["blueprint"]["entities"]:
        # main entity
        if not (name := get_value(entity, "name")):
            continue
        quality = get_value(entity, "quality", default="normal")
        items_counter.update(((name, quality),))

        # entity modules
        for item in get_value(entity, "items", default=[]):
            modules = []
            if name := get_value(item, "id", "name"):
                quality = get_value(item, "id", "quality", default="normal")
                module = (name, quality)
                for in_inventory in get_value(item, "items", "in_inventory", default=[]):
                    if "stack" in in_inventory:
                        modules.append(module)
            items_counter.update(modules)

        # entity grid
        for grid_item in get_value(entity, "grid", default=[]):
            if name := get_value(grid_item, "equipment", "name"):
                quality = get_value(grid_item, "equipment", "quality", default="normal")
                items_counter.update(((name, quality),))

    # tiles
    if tiles := get_value(blueprint, "blueprint", "tiles"):
        items_counter.update((tile["name"], "normal") for tile in tiles)  # tiles are always normal quality

    # sort
    items = dict(items_counter)
    return sorted(
        [{"name": name, "quality": quality, "count": count} for (name, quality), count in items.items()],
        key=lambda i: (-i["count"], i["name"], QUALITY_ORDER[i["quality"]]),
    )


def decode(b64_data: str) -> BlueprintType:
    """Decode a blueprint string.

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
    """Encode a data structure as a blueprint string.

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
