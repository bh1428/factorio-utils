#!/usr/bin/env python3
"""Tests for factorio.bp.common"""

import pytest

import factorio.bp as fbp
from tests.data.blueprints import blueprints

# pylint: disable=missing-function-docstring


@pytest.mark.parametrize("bp_name", blueprints.keys())
def test_decode(bp_name: str):
    test_bp = blueprints[bp_name]
    bp = fbp.decode(test_bp["b64_str"])
    assert bp == test_bp["bp"]


@pytest.mark.parametrize("bp_name", blueprints.keys())
def test_encode(bp_name: str):
    test_bp = blueprints[bp_name]
    b64_str = fbp.encode(test_bp["bp"])
    # due to (supposedly) minor differences in zlib settings
    # the compressed result will not be binary equivalent...
    # lets check by round tripping through decode
    assert fbp.decode(b64_str) == test_bp["bp"]


@pytest.mark.parametrize("bp_name", blueprints.keys())
def test_count_entities(bp_name: str):
    test_bp = blueprints[bp_name]
    entities = fbp.count_entities(test_bp["bp"])
    assert entities == test_bp["entities"]


TEST_DICT = {
    "one": {
        "two": {
            "three": 3,
        },
    },
}
GET_VALUE_PARAMETERS_NO_DEFAULT = (
    (TEST_DICT, ("",), None),
    (TEST_DICT, ("missing",), None),
    (TEST_DICT, ("one",), TEST_DICT["one"]),
    (TEST_DICT, ("one", "two"), TEST_DICT["one"]["two"]),
    (TEST_DICT, ("one", "missing"), None),
    (TEST_DICT, ("one", "two", "three"), TEST_DICT["one"]["two"]["three"]),
    (TEST_DICT, ("one", "two", "missing"), None),
)


@pytest.mark.parametrize("test_dict, keys, expected", GET_VALUE_PARAMETERS_NO_DEFAULT)
def test_get_value_no_default(test_dict, keys, expected):
    value = fbp.get_value(test_dict, *keys)
    assert value == expected


GET_VALUE_PARAMETERS_WITH_DEFAULT = (
    (TEST_DICT, ("",), "default", "default"),
    (TEST_DICT, ("missing",), "default", "default"),
    (TEST_DICT, ("one",), "default", TEST_DICT["one"]),
    (TEST_DICT, ("one", "two"), "default", TEST_DICT["one"]["two"]),
    (TEST_DICT, ("one", "missing"), "default", "default"),
    (TEST_DICT, ("one", "two", "three"), "default", TEST_DICT["one"]["two"]["three"]),
    (TEST_DICT, ("one", "two", "missing"), "default", "default"),
)


@pytest.mark.parametrize("test_dict, keys, default, expected", GET_VALUE_PARAMETERS_WITH_DEFAULT)
def test_get_value_with_default(test_dict, keys, default, expected):
    value = fbp.get_value(test_dict, *keys, default=default)
    assert value == expected


if __name__ == "__main__":
    pytest.main(["-vv", "-s", "tests/bp/test_common.py"])
