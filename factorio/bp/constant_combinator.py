"""factorio.bp.constant_combinator - create a constant combinator from a blueprint"""

import copy
from datetime import datetime
from typing import TypedDict

from factorio.bp.common import BlueprintType, ItemListType

FilterType = TypedDict("FilterType", {"index": int, "name": str, "quality": str, "comparator": str, "count": int})

BLUEPRINT_TEMPLATE = {
    "blueprint": {
        "icons": [{"signal": {"name": "constant-combinator"}, "index": 1}],
        "entities": [
            {
                "entity_number": 1,
                "name": "constant-combinator",
                "position": {"x": 0.0, "y": 0.0},
                "control_behavior": {"sections": {"sections": [{"index": 1, "filters": [], "group": ""}]}},
            }
        ],
        "item": "blueprint",
        "label": "",
        "version": 562949956239363,
    }
}


def create_constant_combinator(name: str, items: ItemListType) -> BlueprintType:
    """Create a constant combinator with the blueprint items as values

    The combinator can be used to set the requests for a Requester Chest.

    Args:
        name (str): name of the blueprint
        items (list[ItemListType]): item list for the blueprint

    Returns:
        BlueprintType: blueprint for a constant combinator
    """

    def create_filter(index: int, name: str, quality: str, count: int) -> FilterType:
        return {"index": index, "name": name, "quality": quality, "comparator": "=", "count": count}

    filters = [create_filter(i, item["name"], item["quality"], item["count"]) for i, item in enumerate(items, 1)]

    blueprint = copy.deepcopy(BLUEPRINT_TEMPLATE)

    sections_0 = blueprint["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]
    sections_0["filters"] = filters
    sections_0["group"] = f"0_{name}_{datetime.now():%Y%m%d_%H%M%S}"

    blueprint["blueprint"]["label"] = f"cc_{name}"

    return blueprint
