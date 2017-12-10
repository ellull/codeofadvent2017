#!/usr/bin/env python
import sys
from operator import xor

class CircularList:
    def __init__(self, values):
        self._values = list(values)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._values[index % len(self._values)]
        elif isinstance(index, slice):
            return list(self._values[i % len(self._values)] for i in xrange(index.start, index.stop, index.step or 1))
        else:
            raise TypeError('list indices must be integers or slices')

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self._values[index % len(self._values)] = value
        elif isinstance(index, slice):
            for i in xrange(index.start, index.stop, index.step or 1):
                self._values[i % len(self._values)] = next(value)
        else:
            raise TypeError('list indices must be integers or slices')

    def __len__(self):
        return len(self._values)

    def __str__(self):
        return str(self._values)

    def __repr__(self):
        return repr(self._values)

def knot_round(lengths, numbers, position, skip):
    for length in lengths:
        index = slice(position, position + length, 1)
        numbers[index] = reversed(numbers[index])
        position += length + skip
        skip += 1

    return numbers, position, skip

def knot_hash(lengths):
    lengths = list(lengths) + [17, 31, 73, 47, 23]
    numbers, position, skip = CircularList(xrange(256)), 0, 0
    for _ in xrange(64):
        numbers, position, skip = knot_round(lengths, numbers, position, skip)
    return ''.join('%02x' % reduce(xor, numbers[i:i + 16]) for i in xrange(0, 256, 16))

if __name__ == '__main__':
    text = next(sys.stdin).strip()

    # First half
    lengths = [int(length) for length in text.split(',')]
    result, position, skip = knot_round(lengths, CircularList(xrange(256)), 0, 0)
    print('Product: %d' % (result[0] * result[1]))

    # Second half
    print('Hash: %s' % knot_hash(ord(char) for char in text))

