"""factorio.bp.constant_combinator - create a constant combinator from a blueprint."""

import copy

from .common import BlueprintType, ConvertEntitiesType, EntityListType, FilterType, count_entities

BLUEPRINT_TEMPLATE: BlueprintType = {
    "blueprint": {
        "icons": [{"signal": {"name": "constant-combinator"}, "index": 1}],
        "entities": [
            {
                "entity_number": 1,
                "name": "constant-combinator",
                "position": {"x": 0.0, "y": 0.0},
                "control_behavior": {"sections": {"sections": [{"index": 1, "filters": []}]}},
            }
        ],
        "item": "blueprint",
        "version": 562949956239363,
    }
}

# some entities must be converted (there are probably more...)
# for example: you need 3 'rail' segments to build one 'curved-rail-a'
CONVERT_ENTITIES: ConvertEntitiesType = {
    # "from_entity": ("to_entity", count)
    "straight-rail": ("rail", 1),
    "curved-rail-a": ("rail", 3),
    "curved-rail-b": ("rail", 3),
}


def create_constant_combinator(signals: EntityListType, name: None | str = None) -> BlueprintType:
    """Create a constant combinator from a set of signals.

    Args:
        name (str): name of the blueprint
        signals (EntityListType): signal list for the blueprint

    Returns:
        BlueprintType: blueprint for a constant combinator
    """

    def create_filter(index: int, name: str, quality: str, count: int) -> FilterType:
        return {"index": index, "name": name, "quality": quality, "comparator": "=", "count": count}

    filters = [
        create_filter(i, signal["name"], signal["quality"], signal["count"]) for i, signal in enumerate(signals, 1)
    ]

    blueprint = copy.deepcopy(BLUEPRINT_TEMPLATE)
    sections_0 = blueprint["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]
    sections_0["filters"] = filters

    if (name is not None) and (name := name.strip()):
        blueprint["blueprint"]["label"] = name

    return blueprint


def blueprint_to_constant_combinator(blueprint: BlueprintType) -> BlueprintType:
    """Create a constant combinator blueprint with all entities in a blueprint as signals.

    Args:
        name (str): name of the constant combinator blueprint
        blueprint (BlueprintType): blueprint to be added as signals to the constant combinator

    Returns:
        BlueprintType: constant combinator blueprint
    """
    name = blueprint["blueprint"]["label"] if "label" in blueprint["blueprint"] else None
    return create_constant_combinator(count_entities(blueprint, CONVERT_ENTITIES), name)
