#!/usr/bin/env python
from days.day1.common import solve
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    ('1122', 3),
    ('1111', 4),
    ('1234', 0),
    ('91212129', 9),
])
def test_1sthalf(puzzle, output):
    assert_equal(solve(puzzle, 1), output)

@parameterized([
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
])
def test_2ndhalf(puzzle, output):
    assert_equal(solve(puzzle, len(puzzle) / 2), output)
