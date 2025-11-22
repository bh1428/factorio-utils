"""Factorio entity list and filters examples."""

from typing import TypedDict

from factorio.bp.common import ItemListType
from factorio.bp.constant_combinator import FilterTypeList

EntityTestDataType = TypedDict("EntityTestDataType", {"entities": ItemListType, "filters": FilterTypeList})

entities: dict[str, EntityTestDataType] = {
    "one_item": {
        "entities": [{"name": "e1", "quality": "normal", "count": 1}],
        "filters": [{"index": 1, "name": "e1", "quality": "normal", "comparator": "=", "count": 1}],
    },
    "two_items": {
        "entities": [
            {"name": "e1", "quality": "normal", "count": 2},
            {"name": "e2", "quality": "normal", "count": 1},
        ],
        "filters": [
            {"index": 1, "name": "e1", "quality": "normal", "comparator": "=", "count": 2},
            {"index": 2, "name": "e2", "quality": "normal", "comparator": "=", "count": 1},
        ],
    },
    "three_items": {
        "entities": [
            {"name": "e3", "quality": "normal", "count": 1},
            {"name": "e2", "quality": "epic", "count": 2},
            {"name": "e1", "quality": "normal", "count": 3},
        ],
        "filters": [
            {"index": 1, "name": "e3", "quality": "normal", "comparator": "=", "count": 1},
            {"index": 2, "name": "e2", "quality": "epic", "comparator": "=", "count": 2},
            {"index": 3, "name": "e1", "quality": "normal", "comparator": "=", "count": 3},
        ],
    },
    "mixed_qualities": {
        "entities": [
            {"name": "efficiency-module-3", "quality": "epic", "count": 2},
            {"name": "speed-module-3", "quality": "rare", "count": 1},
            {"name": "speed-module-3", "quality": "legendary", "count": 1},
            {"name": "assembling-machine-3", "quality": "uncommon", "count": 1},
        ],
        "filters": [
            {"index": 1, "name": "efficiency-module-3", "quality": "epic", "comparator": "=", "count": 2},
            {"index": 2, "name": "speed-module-3", "quality": "rare", "comparator": "=", "count": 1},
            {"index": 3, "name": "speed-module-3", "quality": "legendary", "comparator": "=", "count": 1},
            {"index": 4, "name": "assembling-machine-3", "quality": "uncommon", "comparator": "=", "count": 1},
        ],
    },
}
