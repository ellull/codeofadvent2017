from days.day10 import CircularList, knot_round, knot_hash
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    ((3, 4, 1, 5), (12, 19, 4)),
])
def test_knot_round(lengths, output):
    numbers, position, skip = knot_round(lengths, CircularList(range(5)), 0, 0)
    assert_equal((numbers[0] * numbers[1], position, skip), output)

@parameterized([
    ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
    ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
    ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
    ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e'),
])
def test_knot_hash(text, output):
    assert_equal(knot_hash(text), output)

