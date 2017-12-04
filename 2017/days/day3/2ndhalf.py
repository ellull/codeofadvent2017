#!/usr/bin/env python
import sys
from itertools import dropwhile
from common import spiral

if (len(sys.argv) == 1):
    print("Usage: %s PUZZLE" % sys.argv[0])
    exit(1)

puzzle = int(sys.argv[1])
print(next(dropwhile(lambda cell: cell.value < puzzle, spiral(with_value=True))).value)
