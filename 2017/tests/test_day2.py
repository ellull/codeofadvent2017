#!/usr/bin/env python
from days.day2.common import difference, divisible, solve 
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    ([5, 1, 9, 5], 8),
    ([7, 5, 3], 4),
    ([2, 4, 6, 8], 6),
])
def test_difference(row, output):
    assert_equal(difference(row), output)

@parameterized([
    ([5, 9, 2, 8], 4),
    ([9, 4, 7, 3], 3),
    ([3, 8, 6, 5], 2),
])
def test_divisible(row, output):
    assert_equal(divisible(row), output)

@parameterized([
    ([[5, 1, 9, 5],
      [7, 5, 3], 
      [2, 4, 6, 8]], 18),
])
def test_1sthalf(puzzle, output):
    assert_equal(solve(puzzle, difference), output)

@parameterized([
    ([[5, 9, 2, 8],
      [9, 4, 7, 3], 
      [3, 8, 6, 5]], 9),
])
def test_2ndhalf(puzzle, output):
    assert_equal(solve(puzzle, divisible), output)

