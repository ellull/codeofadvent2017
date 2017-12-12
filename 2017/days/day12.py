#!/usr/bin/env python
import re
import sys
import networkx as nx

parser = re.compile("^(\d+) <-> (\d+(?:, \d+)*)")
graph = nx.Graph()
for line in sys.stdin:
    orig, dests = parser.match(line).groups()
    graph.add_edges_from((orig, dest) for dest in dests.split(', '))

print('Programs connected to ID 0: %d' % len(nx.node_connected_component(graph, '0')))
print('Number of groups: %d' % len(list(nx.connected_components(graph))))
