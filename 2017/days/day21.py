#!/usr/bin/env python
import re
import fileinput
from math import sqrt

permutations = {
        5: (
            (0, 1, 2, 3, 4),
            (3, 0, 2, 4, 1),  # 1st rotation
            (4, 3, 2, 1, 0),  # 2nd rotation
            (1, 4, 2, 0, 3),  # 3rd rotation
            ),
        11: (
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            (8, 4, 0, 3, 9, 5, 1, 7, 10, 6, 2),  # 1st rotation
            (10, 9, 8, 3, 6, 5, 4, 7, 2, 1, 0),  # 2nd rotation
            (2, 6, 10, 3, 1, 5, 9, 7, 0, 4, 8),  # 3rd rotation
            ),
        }

flips = {
        5: (
            (0, 1, 2, 3, 4),
            (1, 0, 2, 4, 3),  # Horizontal flip
            (3, 4, 2, 0, 1),  # Vertical flip
            ),
        11: (
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
            (2, 1, 0, 3, 6, 5, 4, 7, 10, 9, 8),  # Horizontal flip
            (8, 9, 10, 3, 4, 5, 6, 7, 0, 1, 2),  # Vertical flip
            ),
        }



def rotate_and_flip(pattern):
    rotations = [pattern]
    for permutation in permutations[len(pattern)]:
        for flip in flips[len(pattern)]:
            rotations.append(''.join(pattern[flip[permutation[i]]] for i in xrange(len(pattern))))
    return set(rotations)

def parse(line):
    input, output = parse.re.match(line).groups()
    return [(variation, output) for variation in rotate_and_flip(input)]
parse.re = re.compile(r'^([.#/]+) => ([.#/]+)$')

def split(grid):
    grid = grid.split('/')
    size = len(grid)
    chunk_size = 2 if size % 2 == 0 else 3

    chunks = []
    for x in xrange(0, size, chunk_size):
        for y in xrange(0, size, chunk_size):
            chunks.append('/'.join(line[x: x + chunk_size] for line in grid[y: y + chunk_size]))

    return chunks

def join(rules):
    i, j, rules = 0, 0, list(rules)

    side = int(sqrt(len(rules)))
    size = len(rules[0].split('/')) * side
    result = ['',] * size

    for a in xrange(side):
        j = 0
        for b in xrange(side):
            for line in rules[i].split('/'):
                result[j] += line
                j += 1
            i += 1

    return '/'.join(result)

if __name__ == '__main__':
    rules = dict(rule for line in fileinput.input() for rule in parse(line))

    grid = '.#./..#/###'
    for i in xrange(1, 19):
        grid = join(rules[pattern] for pattern in split(grid))
        if i == 5:
            print('%d pixels stay on after %d iterations' % (sum(map(lambda p: p == '#', grid)), i))
    print('%d pixels stay on after %d iterations' % (sum(map(lambda p: p == '#', grid)), i))
