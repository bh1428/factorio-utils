#!/usr/bin/env python3
"""Tests for factorio.bp.constant_combinator."""

import pytest

import factorio.bp as fbp
from tests.data.blueprints import blueprints
from tests.data.entities import entities

# pylint: disable=missing-function-docstring


def test_no_name():
    bp = fbp.create_constant_combinator([])
    assert "label" not in bp["blueprint"]


def test_empty_name_is_ignored():
    bp = fbp.create_constant_combinator([], "  ")
    assert "label" not in bp["blueprint"]


def test_label_contains_name():
    name = "test_label_contains_name"
    bp = fbp.create_constant_combinator([], name)
    assert name in bp["blueprint"]["label"]


def test_empty_entities_list():
    name = "test_empty_entities_list"
    bp = fbp.create_constant_combinator([], name)
    assert len(bp["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]["filters"]) == 0


def test_results_can_be_equal():
    name = "test_results_can_be_equal"
    bp1 = fbp.create_constant_combinator([], name)
    bp2 = fbp.create_constant_combinator([], name)
    assert bp1 == bp2


def test_results_can_be_equal_but_are_unique():
    name = "test_results_can_be_equal_but_are_unique"
    bp1 = fbp.create_constant_combinator([], name)
    bp2 = fbp.create_constant_combinator([], name)
    assert bp1 is not bp2


@pytest.mark.parametrize("entity", entities.keys())
def test_entities(entity: str):
    test_entity = entities[entity]
    bp = fbp.create_constant_combinator(test_entity["entities"])
    assert (
        bp["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]["filters"]
        == test_entity["filters"]
    )


@pytest.mark.parametrize("bp_name", blueprints.keys())
def test_blueprint_to_constant_combinator_check_label(bp_name):
    bp = blueprints[bp_name]
    cc_bp = fbp.blueprint_to_constant_combinator(bp["bp"])
    if "label" in bp["bp"]["blueprint"]:
        assert cc_bp["blueprint"]["label"] == bp["bp"]["blueprint"]["label"]
    else:
        assert "label" not in cc_bp["blueprint"]


@pytest.mark.parametrize("bp_name", blueprints.keys())
def test_blueprint_to_constant_combinator_check_entities(bp_name):
    bp = blueprints[bp_name]
    cc_bp = fbp.blueprint_to_constant_combinator(bp["bp"])
    filters = cc_bp["blueprint"]["entities"][0]["control_behavior"]["sections"]["sections"][0]["filters"]
    entities_from_filters = [{"name": f["name"], "quality": f["quality"], "count": f["count"]} for f in filters]
    if "entities_translated" not in bp:
        assert entities_from_filters == bp["entities"]
    else:
        assert entities_from_filters == bp["entities_translated"]


if __name__ == "__main__":
    pytest.main(["-vv", "tests/bp/test_constant_combinator.py"])
