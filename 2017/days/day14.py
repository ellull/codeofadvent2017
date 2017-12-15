#!/usr/bin/env python
import sys
from day10 import knot_hash

def hex_to_bits(digits):
    lshifts = [3, 2, 1, 0]
    return [bool(int(digit, base=16) & (1 << lshift)) for digit in digits for lshift in lshifts]

def sparse(bool_list, val):
    return {n: val for (n, bit) in enumerate(bool_list) if bit}

class Grid(object):
    def __init__(self, seed, exporter=None):
        # Initialize grid
        print("Populating blocks...")
        self.blocks = {y: sparse(hex_to_bits(knot_hash('%s-%d' % (seed, y))), 0) for y in xrange(128)}

        # Group the blocks
        print("Grouping blocks...")
        self.num_groups = 0
        exporter.start(self)
        for (y, row) in self.blocks.iteritems():
            for (x, group) in row.iteritems():
                if group == 0:
                    exporter.next(self)
                    self.num_groups += 1
                    self.flood(x, y, self.num_groups, exporter.flood)
        
    def __len__(self):
        return sum(len(row) for row in self.blocks.itervalues())

    def get(self, x, y):
        if not (0 <= y <= 127 and 0 <= x <= 127):
            return None
        return self.blocks[y].get(x, None)

    def set(self, x, y, val):
        if not (0 <= y <= 127 and 0 <= x <= 127):
            raise IndexError('(%s, %s): indexes must be between 0 and 127' % (x, y))
        self.blocks[y][x] = val

    def adjacents(self, coords):
        return [(xx, yy) for (x, y) in coords for (xx, yy) in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)) if self.get(xx, yy) is not None]

    # It would have been better to use recursion but as Pyhton does not have
    # tail-recursion optimization it was raising exceptions
    def flood(self, x, y, group, callback=None):
        adjacents, prev_group = [(x, y)], self.get(x, y)
        while len(adjacents) > 0:
            if callback is not None:
                callback(adjacents, group)
            for xx, yy in adjacents:
                self.set(xx, yy, group)
            adjacents = filter(lambda (ax, ay): self.get(ax, ay) == prev_group, self.adjacents(adjacents))


if __name__ == '__main__':
    grid = Grid(sys.argv[1])
    print('Number of blocks: %d' % len(grid))
    print('Number of groups: %d' % grid.num_groups)

