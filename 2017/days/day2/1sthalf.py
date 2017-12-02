#!/usr/bin/env python
import fileinput
from common import solve, difference

puzzle = [map(int, line.split("\t")) for line in fileinput.input()]
print(solve(puzzle, difference))
