"""factorio.bp - blueprints.

The structure of a Factorio blueprint is described here: https://wiki.factorio.com/Blueprint_string_format:
    A blueprint string is a JSON representation of the blueprint, compressed with zlib deflate using compression
    level 9 and then encoded using base64 with a version byte in front of the encoded string. The version byte
    is currently 0 (for all Factorio versions through 2.0). So to get the JSON representation of a blueprint
    from a blueprint string, skip the first byte, base64 decode the string, and finally decompress using zlib inflate.
"""

from .common import BlueprintType, EntityListType, FilterTypeList, count_entities, decode, encode, get_value
from .constant_combinator import FilterType, blueprint_to_constant_combinator, create_constant_combinator

__all__ = [
    "BlueprintType",
    "EntityListType",
    "FilterType",
    "FilterTypeList",
    "count_entities",
    "create_constant_combinator",
    "decode",
    "encode",
    "get_value",
    "blueprint_to_constant_combinator",
]
