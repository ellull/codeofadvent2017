from days.day9 import parse, skip_garbage
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    ('{}', (1, 0)),
    ('{{{}}}', (6, 0)),
    ('{{},{}}', (5, 0)),
    ('{{{},{},{{}}}}', (16, 0)),
    ('{<a>,<a>,<a>,<a>}', (1, 4)),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', (9, 8)),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', (9, 0)),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', (3, 17)),
])
def test_score(puzzle, output):
    assert_equal(parse(iter(puzzle)), output)

@parameterized([
    ('<>', 0),
    ('<random characters>', 17),
    ('<<<<>', 3),
    ('<{!>}>', 2),
    ('<!!>', 0),
    ('<!!!>>', 0),
    ('<{o"i!a,<{i<a>', 10),
])
def test_skip_garbage(garbage, output):
    iterable = iter(garbage)
    next(iterable)  # Skip the first '<'
    assert_equal(skip_garbage(iterable), output)

