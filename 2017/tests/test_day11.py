from days.day11 import ORIGIN, scan, walk
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    (('ne', 'ne', 'ne'), 3),
    (('ne', 'ne', 'sw', 'sw'), 0),
    (('ne', 'ne', 's', 's'), 2),
    (('se', 'sw', 'se', 'sw', 'sw'), 3),
])
def test_1sthalf(steps, output):
    assert_equal(reduce(walk, steps, ORIGIN).distance(ORIGIN), output)

@parameterized([
    (('ne', 'ne', 'ne'), 3),
    (('ne', 'ne', 'sw', 'sw'), 2),
    (('ne', 'ne', 's', 's'), 2),
    (('se', 'sw', 'se', 'sw', 'sw'), 3),
])
def test_2ndhalf(steps, output):
    assert_equal(max(map(ORIGIN.distance, scan(walk, steps, ORIGIN))), output)

