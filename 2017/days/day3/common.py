from itertools import count, islice
from math import sqrt, ceil

class Point:
    def __init__(self, x, y, n = 0):
        self.x = x
        self.y = y
        self.n = n

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def is_adjacent_to(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return "Point({self.x:d}, {self.y:d}, {self.n:d})".format(self=self)

STEPS = (
    Point(1, 0),  # Right
    Point(0, 1),  # Up
    Point(-1, 0), # Left
    Point(0, -1), # Down
)

def spiral():
    return (STEPS[i % 4] for i in count() for j in xrange(i // 2 + 1))

def stress_spiral():
    points = [Point(0, 0, 1)]
    for p in spiral():
        yield points[-1].n
        point = points[-1] + p
        point.n = sum(i.n for i in points if point.is_adjacent_to(i))
        points.append(point)

def manhattan_distance(n):
    return reduce(lambda x, y: x + y, islice(spiral(), n - 1), Point(0, 0)).manhattan_distance(Point(0, 0))

