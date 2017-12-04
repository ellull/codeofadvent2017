from days.day4.common import is_valid, is_valid_v2 
from nose.tools import assert_equal
from parameterized import parameterized

@parameterized([
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
])
def test_valid_passphrase(passphrase, output):
    assert_equal(is_valid(passphrase), output)

@parameterized([
    ('abcde fghij', True),
    ('oiii ioii iioi iiio', False),
])
def test_valid_passphrase_v2(passphrase, output):
    assert_equal(is_valid_v2(passphrase), output)

