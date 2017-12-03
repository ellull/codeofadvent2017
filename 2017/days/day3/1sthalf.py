#!/usr/bin/env python
import sys
from common import manhattan_distance

if (len(sys.argv) == 1):
    print("Usage: %s PUZZLE" % sys.argv[0])
    exit(1)
                
print(manhattan_distance(int(sys.argv[1])))
