#!/usr/bin/env python
import sys

class Grid(object):
    def __init__(self, initial_state):
        self.nodes = {}
        for y, line in enumerate(initial_state):
            for x, char in enumerate(line.strip()):
                self.nodes[(x - 12, y - 12)] = (2 if char == '#' else 0)

    def get(self, pos):
        return self.nodes.get(pos, False)

    def set(self, pos, value):
        self.nodes[pos] = value


class Virus(object):
    DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))

    def __init__(self, grid, change_directions = {0: -1, 2: 1}, transitions = {0: 2, 2: 0}):
        self.position = (0, 0)
        self.direction = 0
        self.change_directions = change_directions
        self.transitions = transitions

        self.grid = grid

    def burst(self):
        node_status = self.grid.get(self.position)

        self.direction = (self.direction + self.change_directions[node_status]) % 4

        self.grid.set(self.position, self.transitions[node_status])

        direction = Virus.DIRECTIONS[self.direction]
        self.position = (self.position[0] + direction[0], self.position[1] + direction[1])

        return self.transitions[node_status] == 2


if __name__ == '__main__':
    initial_state = list(sys.stdin)

    virus = Virus(Grid(initial_state))
    print('Virus has infected a node %d times' % sum(virus.burst() for _ in xrange(10000)))

    virus = Virus(Grid(initial_state), {0: -1, 1: 0, 2: 1, 3: 2}, {0: 1, 1: 2, 2: 3, 3: 0})
    print('Virus has infected a node %d times' % sum(virus.burst() for _ in xrange(10000000)))


