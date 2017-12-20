#!/usr/bin/env python
import re
import sys
from itertools import combinations, product
from collections import defaultdict
from math import sqrt
from pprint import pprint

class Point(object):
    COORDS = set(('x', 'y', 'z'))

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __len__(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __repr__(self):
        return 'Point(%d, %d, %d)' % (self.x, self.y, self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __getitem__(self, item):
        if item in Point.COORDS:
            return self.__dict__[item]

class Particle(object):
    def __init__(self, number, position, velocity, acceleration):
        self.number = number
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def __repr__(self):
        return 'Particle(%d, %s, %s, %s)' % (self.number, self.position, self.velocity, self.acceleration)

    def __hash__(self):
        return hash(self.number)

    def __eq__(self, other):
        return self.number == other.number

    def colide_time(self, other):
        def solve(acc, vel, pos):
            a, b, c = acc / 2, vel + acc / 2, pos
            if a == 0.0:
                if b == 0.0:
                    return None if c == 0.0 else set()
                else:
                    return set(filter(lambda i: i > 0, (-c / b,)))
            common = b * b - 4 * a * c
            if common < 0:
                return set()
            return set(filter(lambda i: i > 0, ((-b + sqrt(common)) / (2 * a), (-b - sqrt(common)) / (2 * a))))

        solutions = None
        acceleration = self.acceleration - other.acceleration
        velocity = self.velocity - other.velocity
        position = self.position - other.position
        for coord in Point.COORDS:
            sols = solve(acceleration[coord], velocity[coord], position[coord]) 
            if sols is not None:
                solutions = solutions & sols if solutions is not None else sols

        if len(solutions) != 1:
            return None
        solution = next(iter(solutions))
        return solution if solution.is_integer() else None


def parse(i, line):
    ns = map(int, parse.re.match(line).groups())
    return Particle(i, Point(*ns[0:3]), Point(*ns[3:6]), Point(*ns[6:9]))
parse.re = re.compile(r'^p=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, v=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>, a=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>')

if __name__ == '__main__':
    particles = [parse(i, line) for i, line in enumerate(sys.stdin)]
    particles.sort(key = lambda particle: len(particle.position))
    particles.sort(key = lambda particle: len(particle.velocity))
    particles.sort(key = lambda particle: len(particle.acceleration))
    print('Particle that will stay closer to <0, 0, 0> is particle #%d' % particles[0].number)

    destroyed_particles = set()
    may_colide = set(combinations(particles, 2))
    while len(may_colide) > 0:
        # Calculate when particles may colide
        collisions = defaultdict(set)
        for pair in may_colide:
            colide_time = pair[0].colide_time(pair[1])
            if colide_time is not None:
                collisions[colide_time].add(pair)

        # Add the particles that colide first to the destroyed particles set
        first_collisions = set(particle for pair in collisions.pop(min(collisions.iterkeys())) for particle in pair)
        destroyed_particles |= first_collisions

        # Keep the pairs that may colide only if none of the two particles
        # colided at the first collision
        may_colide = set(pair for pair_set in collisions.itervalues() for pair in pair_set if pair[0] not in first_collisions and pair[1] not in first_collisions)

    print("After all collisions, only %d particles are left" % (len(particles) - len(destroyed_particles)))

