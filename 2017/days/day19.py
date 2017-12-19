#!/usr/bin/env python
import fileinput
from collections import namedtuple

class Path(object):
    Position = namedtuple('Position', ['x', 'y'])
    UP = Position(0, -1)
    DOWN = Position(0, 1)
    RIGHT = Position(1, 0)
    LEFT = Position(-1, 0)

    def __init__(self, path):
        self.path = [line[:-1] for line in path]
        self.position = Path.Position(self.path[0].index('|'), -1)
        self.direction = Path.DOWN

    def get(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        return self.path[y][x]

    def current(self):
        return self.get(*self.position)

    def next(self):
        self.position = Path.Position(self.position.x + self.direction.x, self.position.y + self.direction.y)
        try:
            char = self.current()
            if char == '+':
                self._change_direction()
            elif char == ' ':
                raise StopIteration
            return char
        except IndexError:
            raise StopIteration

    def _change_direction(self):
        for adjacent in (Path.UP, Path.DOWN, Path.RIGHT, Path.LEFT):
             if adjacent.x != -self.direction.x and adjacent.y != -self.direction.y and self.get(self.position.x + adjacent.x, self.position.y + adjacent.y) != ' ':
                 self.direction = adjacent
                 break

    def __iter__(self):
        return self

    def __str__(self):
        return "\n".join(self.path)

if __name__ == '__main__':
    path = Path(fileinput.input())

    # Walk the path
    letters, steps = [], 0
    for char in path:
        steps += 1
        if char not in '|-+':
            letters.append(char)

    print('Letters visited in order: %s' % "".join(letters))
    print('Packet needed %d steps' % steps)

