#!/usr/bin/env python
import sys
from itertools import dropwhile
from common import stress_spiral

if (len(sys.argv) == 1):
    print("Usage: %s PUZZLE" % sys.argv[0])
    exit(1)
                
print(next(dropwhile(lambda x: x <= int(sys.argv[1]), stress_spiral())))
