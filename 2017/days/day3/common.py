from itertools import count, islice

class Point:
    def __init__(self, x, y, value = 0):
        self._x = x
        self._y = y
        self.value = value

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)

    def __repr__(self):
        return "Point({self._x:d}, {self._y:d}, {self.value:d})".format(self=self)

    def manhattan_distance(self, other):
        return abs(self._x - other._x) + abs(self._y - other._y)

    def is_adjacent_to(self, other):
        return (self._x - other._x) ** 2 + (self._y - other._y) ** 2 < 4.0

STEPS = (
    Point(1, 0),  # Right
    Point(0, 1),  # Up
    Point(-1, 0), # Left
    Point(0, -1), # Down
)

def spiral(with_value=False):
    cell = Point(0, 0, 1)
    cells = [cell]
    for step in (STEPS[i % 4] for i in count() for j in xrange(i // 2 + 1)):
        yield cell
        cell = cell + step
        if with_value:
            cell.value = sum(other.value for other in cells if cell.is_adjacent_to(other))
            cells.append(cell)

def manhattan_distance(n):
    return next(islice(spiral(), n - 1, n)).manhattan_distance(Point(0, 0))

