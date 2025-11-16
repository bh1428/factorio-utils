#!/usr/bin/env python3
"""Tests for factorio.bp"""

import pytest

import factorio.bp as fbp
from tests.data.blueprints import bps

# pylint: disable=missing-function-docstring


@pytest.mark.parametrize("bp_name", bps.keys())
def test_decode(bp_name: str):
    test_bp = bps[bp_name]
    bp = fbp.decode(test_bp["b64_str"])
    assert bp == test_bp["bp"]


@pytest.mark.parametrize("bp_name", bps.keys())
def test_encode(bp_name: str):
    test_bp = bps[bp_name]
    b64_str = fbp.encode(test_bp["bp"])
    # due to (supposedly) minor differences in zlib settings
    # the compressed result will not be binary equivalent...
    # lets check by round tripping through decode
    assert fbp.decode(b64_str) == test_bp["bp"]


if __name__ == "__main__":
    pytest.main(["-vv"])
