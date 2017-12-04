#!/usr/bin/env python
from days.day3.common import spiral, manhattan_distance
from itertools import islice
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
])
def test_manhattan_distance(num, output):
    assert_equal(manhattan_distance(num), output)

@parameterized([
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 5),
    (12, 57),
    (23, 806),
])
def test_stress(num, output):
    assert_equal(next(islice(spiral(), num - 1, num)).value, output)
