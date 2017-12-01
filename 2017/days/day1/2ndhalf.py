#!/usr/bin/env python
import sys
from common import solve

puzzle = sys.argv[1]
print(solve(puzzle, len(puzzle) / 2))
