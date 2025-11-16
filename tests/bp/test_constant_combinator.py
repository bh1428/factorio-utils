#!/usr/bin/env python3
"""Tests for factorio.bp.constant_combinator"""

import pytest

import factorio.bp as fbp

# pylint: disable=missing-function-docstring


def test_group_contains_name():
    name = "test_group_contains_name"
    bp = fbp.create_constant_combinator(name, [])
    assert name in bp["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]["group"]


def test_label_contains_name():
    name = "test_label_contains_name"
    bp = fbp.create_constant_combinator(name, [])
    assert name in bp["blueprint"]["label"]


def test_empty_entities_list():
    name = "test_empty_entities_list"
    bp = fbp.create_constant_combinator(name, [])
    assert len(bp["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]["filters"]) == 0


def test_results_can_be_equal():
    name = "test_results_can_be_equal"
    bp1 = fbp.create_constant_combinator(name, [])
    bp2 = fbp.create_constant_combinator(name, [])
    assert bp1 == bp2


def test_results_can_be_equal_but_are_unique():
    name = "test_results_can_be_equal_but_are_unique"
    bp1 = fbp.create_constant_combinator(name, [])
    bp2 = fbp.create_constant_combinator(name, [])
    assert bp1 is not bp2


TEST_ENTITIES_DATA = (
    (
        [{"name": "e1", "quality": "normal", "count": 1}],
        [{"index": 1, "name": "e1", "quality": "normal", "comparator": "=", "count": 1}],
    ),
    (
        [
            {"name": "e1", "quality": "normal", "count": 2},
            {"name": "e2", "quality": "normal", "count": 1},
        ],
        [
            {"index": 1, "name": "e1", "quality": "normal", "comparator": "=", "count": 2},
            {"index": 2, "name": "e2", "quality": "normal", "comparator": "=", "count": 1},
        ],
    ),
    (
        [
            {"name": "e3", "quality": "normal", "count": 1},
            {"name": "e2", "quality": "epic", "count": 2},
            {"name": "e1", "quality": "normal", "count": 3},
        ],
        [
            {"index": 1, "name": "e3", "quality": "normal", "comparator": "=", "count": 1},
            {"index": 2, "name": "e2", "quality": "epic", "comparator": "=", "count": 2},
            {"index": 3, "name": "e1", "quality": "normal", "comparator": "=", "count": 3},
        ],
    ),
    (
        [
            {"name": "efficiency-module-3", "quality": "epic", "count": 2},
            {"name": "speed-module-3", "quality": "rare", "count": 1},
            {"name": "speed-module-3", "quality": "legendary", "count": 1},
            {"name": "assembling-machine-3", "quality": "uncommon", "count": 1},
        ],
        [
            {"index": 1, "name": "efficiency-module-3", "quality": "epic", "comparator": "=", "count": 2},
            {"index": 2, "name": "speed-module-3", "quality": "rare", "comparator": "=", "count": 1},
            {"index": 3, "name": "speed-module-3", "quality": "legendary", "comparator": "=", "count": 1},
            {"index": 4, "name": "assembling-machine-3", "quality": "uncommon", "comparator": "=", "count": 1},
        ],
    ),
)


@pytest.mark.parametrize("entities, expected_filters", TEST_ENTITIES_DATA)
def test_entities(entities, expected_filters):
    bp = fbp.create_constant_combinator("", entities)
    assert bp["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]["filters"] == expected_filters


if __name__ == "__main__":
    pytest.main(["-vv", "tests/bp/test_constant_combinator.py"])
