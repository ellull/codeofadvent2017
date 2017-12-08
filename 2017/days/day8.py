#!/usr/bin/env python
import re
import sys
import operator
from collections import defaultdict

parser = re.compile(r"^(?P<reg>\w+) (?P<op>inc|dec) (?P<val>-?\d+) if (?P<if_reg>\w+) (?P<if_op>.*) (?P<if_val>-?\d+)$")

ops = {
    '==': operator.eq,
    '!=': operator.ne,
    '>':  operator.gt,
    '>=': operator.ge,
    '<':  operator.lt,
    '<=': operator.le,
}

registers = defaultdict(int)
maximum = 0
for line in sys.stdin:
    (reg, op, val, if_reg, if_op, if_val) = parser.match(line).groups()
    if ops[if_op](registers[if_reg], int(if_val)):
        registers[reg] += (1 if op == "inc" else -1) * int(val)
        maximum = max(maximum, registers[reg])

print("Maximum register value at the end: %d" % max(registers.itervalues()))
print("Maximum register value during the process: %d" % maximum)
