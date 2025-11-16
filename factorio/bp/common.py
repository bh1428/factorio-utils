"""factorio.bp.common - common functionality"""

import base64
import json
import zlib
from typing import Any

type BlueprintType = dict[str, dict[str, Any]]


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
