#!/usr/bin/env python3
import fileinput
from collections import defaultdict

class OrbitMap(object):
    def __init__(self, root_node):
        self.root_node = root_node
        self.nodes = set()
        self.edges = defaultdict(set)

    def add_edge(self, a, b):
        self.nodes.add(a)
        self.nodes.add(b)
        self.edges[a].add(b)
        self.edges[b].add(a)

    def path(self, start, end, path = None):
        #print("->", path, start, end)
        if path is None:
            path = []
        path.append(start)

        if start == end:
            return path

        if start not in self.edges:
            return None

        for node in self.edges[start]:
            if node not in path:
                newpath = self.path(node, end, list(path))
                if newpath:
                    return newpath
        return None

    def orbits(self, node, start = None):
        return len(self.path(start or self.root_node, node)) - 1

    def orbital_transfers(self, start, end):
        return self.orbits(orbit_map.path(self.root_node, end)[-2], start=orbit_map.path(self.root_node, start)[-2])


orbit_map = OrbitMap("COM")

orbit_map.add_edge("COM", "B")
orbit_map.add_edge("B", "C")
orbit_map.add_edge("C", "D")
orbit_map.add_edge("D", "E")
orbit_map.add_edge("E", "F")
orbit_map.add_edge("B", "G")
orbit_map.add_edge("G", "H")
orbit_map.add_edge("D", "I")
orbit_map.add_edge("E", "J")
orbit_map.add_edge("J", "K")
orbit_map.add_edge("K", "L")

assert orbit_map.orbits("D") == 3
assert orbit_map.orbits("L") == 7
assert orbit_map.orbits("COM") == 0


if __name__ == "__main__":
    orbit_map = OrbitMap("COM")
    for line in fileinput.input():
        orbit_map.add_edge(*line.strip().split(")"))

    print("Total orbits: {:d}".format(sum(orbit_map.orbits(node) for node in orbit_map.nodes)))
    print("Orbital transfers: {:d}".format(orbit_map.orbital_transfers("YOU", "SAN")))
