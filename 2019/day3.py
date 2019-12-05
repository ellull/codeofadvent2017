#!/usr/bin/env python
import fileinput
from itertools import takewhile
from typing import (Iterable, Tuple)

Path = Iterable[Tuple[str, int]]
Position = Tuple[int, int]


def parse_input(input: str) -> Path:
    return map(lambda step: (step[0], int(step[1:])), input.split(","))

def positions(path: Path) -> Iterable[Position]:
    x = y = 0

    positions = []
    for direction, length in path:
        for _ in range(length):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            positions.append((x, y))
    return positions

def intersections(cable1: Iterable[Position], cable2: Iterable[Position]) -> Iterable[Position]:
    return set(cable1).intersection(set(cable2))

def manhattan_distance(position: Position) -> int:
    return abs(position[0]) + abs(position[1])

def steps_until(intersection: Position, positions: Iterable[Position]) -> int:
    steps = 0
    for position in positions:
        steps += 1
        if position == intersection:
            return steps
    return -1

def closest_intersection_distance(positions1: Iterable[Position], positions2: Iterable[Position]) -> int:
    return min(map(manhattan_distance, intersections(positions1, positions2)))

def shortest_steps(positions1: Iterable[Position], positions2: Iterable[Position]) -> int:
    return min(steps_until(intersection, positions1) + steps_until(intersection, positions2) for intersection in intersections(positions1, positions2))


if __name__ == "__main__":
    assert closest_intersection_distance(positions(parse_input("R75,D30,R83,U83,L12,D49,R71,U7,L72")),
                                         positions(parse_input("U62,R66,U55,R34,D71,R55,D58,R83"))) == 159
    assert closest_intersection_distance(positions(parse_input("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")),
                                         positions(parse_input("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))) == 135

    input = fileinput.input()
    cable1 = positions(parse_input(input.readline()))
    cable2 = positions(parse_input(input.readline()))

    print("Closest intersection: {:d}".format(closest_intersection_distance(cable1, cable2)))


    assert shortest_steps(positions(parse_input("R75,D30,R83,U83,L12,D49,R71,U7,L72")),
                          positions(parse_input("U62,R66,U55,R34,D71,R55,D58,R83"))) == 610
    assert shortest_steps(positions(parse_input("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")),
                          positions(parse_input("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))) == 410

    print("Shortest steps: {:d}".format(shortest_steps(cable1, cable2)))
