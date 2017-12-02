#!/usr/bin/env python
import fileinput
from common import solve, divisible

puzzle = [map(int, line.split("\t")) for line in fileinput.input()]
print(solve(puzzle, divisible))
