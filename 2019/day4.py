#!/usr/bin/env python3
import fileinput
from collections import Counter

def match_rules(password: str) -> bool:
    if len(password) != 6:
        return False

    prev_digit = password[0]
    two_consecutive_digits = False
    for digit in password[1:]:
        if digit == prev_digit:
            two_consecutive_digits = True
        if digit < prev_digit:
            return False
        prev_digit = digit

    return two_consecutive_digits

def match_additional_rule(password: str) -> bool:
    return any(map(lambda x: x == 2, Counter(password).values()))

if __name__ == "__main__":
    c = Counter("1234")

    assert match_rules("111111")
    assert not match_rules("223450")
    assert not match_rules("123789")

    start, stop = fileinput.input().readline().split("-")

    matching_passwords = [str(password) for password in range(int(start), int(stop) + 1) if match_rules(str(password))]

    print("Matching password: {:d}".format(len(matching_passwords)))

    assert match_additional_rule("112233")
    assert not match_additional_rule("123444")
    assert match_additional_rule("111122")

    print("Matching strict password: {:d}".format(len([password for password in matching_passwords if match_additional_rule(password)])))
