#!/usr/bin/env python
import fileinput
import re
from collections import defaultdict
from anytree import Node, RenderTree

nodes = {}
def get_node(name):
    node = nodes.get(name)
    if not node:
        node = Node(name)
        nodes[name] = node
    return node

def parse(lines):
    def children(children):
        return children.split(', ') if children else []

    format = re.compile("^(?P<name>\w+) \((?P<weight>\d+)\)(?: -> (?P<children>.+))?$")
    for line in lines:
        values = format.match(line.strip())
        node = get_node(values.group('name'))
        node.weight = int(values.group('weight'))
        for child in children(values.group('children')):
            get_node(child).parent = node
    return node.root

def balance(node, weight = 0):
    def tower_weight(node):
        return node.weight + sum(descendant.weight for descendant in node.descendants)

    # Find the node's children with its weight
    weights = defaultdict(list)
    for child in node.children:
        weights[tower_weight(child)].append(child)

    # If all children weithgs are equal, we've found the unbalanced node
    if len(weights) == 1:
        child_weight, children = weights.items()[0]
        return (node, weight - child_weight * len(children))

    # Call balance recursively to balance
    (_, unbalanced_child), (balance_weight, _) = tuple(sorted(weights.items(), key = lambda (k, v): len(v)))
    return balance(unbalanced_child[0], balance_weight)
        

root = parse(fileinput.input())
print("Program at the bottom is: %s" % root.name)

unbalanced_node, new_weight = balance(root)
print("To balance the tower, node '%s' should weight %d" % (unbalanced_node.name, new_weight))

