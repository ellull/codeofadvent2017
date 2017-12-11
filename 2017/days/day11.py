#!/usr/bin/env python
import sys

# Based on https://www.redblobgames.com/grids/hexagons/
class Hex(object):
    # See https://www.redblobgames.com/grids/hexagons/#neighbors-cube
    __directions = {
        'n': (0, 1, -1),
        'ne': (1, 0, -1),
        'se': (1, -1, 0),
        's': (0, -1, 1),
        'sw': (-1, 0, 1),
        'nw': (-1, 1, 0),
    }

    # Based on https://www.redblobgames.com/grids/hexagons/#coordinates-cube
    def __init__(self, x, y, z):
        assert x + y + z == 0
        self.x = x
        self.y = y
        self.z = z

    def walk(self, direction):
        x, y, z = Hex.__directions[direction]
        return Hex(self.x + x, self.y + y, self.z + z)

    # See https://www.redblobgames.com/grids/hexagons/#distances-cube
    def distance(self, other):
        return (abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)) / 2

    def __repr__(self):
        return 'Hex(%d, %d, %d)' % (self.x, self.y, self.z)

ORIGIN = Hex(0, 0, 0)
walk = lambda x, s: x.walk(s)

def scan(function, iterable, initializer):
    accum = initializer
    yield accum
    for x in iterable:
        accum = function(accum, x)
        yield accum
    

if __name__ == '__main__':
    steps = next(sys.stdin).strip().split(',')
    print('Distance to child: %d' % reduce(walk, steps, ORIGIN).distance(ORIGIN))
    print('Furthest distence: %d' % max(map(ORIGIN.distance, scan(walk, steps, ORIGIN))))

