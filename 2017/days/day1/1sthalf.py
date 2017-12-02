#!/usr/bin/env python
import sys
from common import solve

if (len(sys.argv) == 1):
    print("Usage: %s PUZZLE" % sys.argv[0])
    exit(1)

print(solve(sys.argv[1], 1))
