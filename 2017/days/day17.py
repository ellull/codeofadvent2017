#!/usr/bin/env python
import sys
from collections import deque

step = int(sys.argv[1])

# Part 1
spinlock, position = [0], 0
for i in xrange(1, 2018):
    position = ((position + step) % i) + 1
    spinlock.insert(position, i)

print('Item after 2017 is %d' % spinlock[spinlock.index(2017) + 1])

# Part 2
position, answer = 0, None
for i in xrange(1, 50000001):
    position = ((position + step) % i) + 1
    if position == 1:
        answer = i

print('Item after 0 is %d' % answer)
