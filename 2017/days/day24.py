#!/usr/bin/env python
import sys

class Bridge(object):
    def __init__(self):
        self.components = []
        self.last_port = 0
        self.strength = 0

    def append(self, component):
        new = Bridge()
        new.components = self.components + [component]
        new.strength = self.strength + sum(component)
        new.last_port = component[0] if component[1] == self.last_port else component[1]
        return new 

    def is_connectable_with(self, component):
        return self.last_port in component

    def __len__(self):
        return len(self.components)

    def __gt__(self, other):
        return len(self) > len(other) or (len(self) == len(other) and self.strength > other.strength)

    def __repr__(self):
        return '--'.join('%d/%d' % component for component in self.components)

    @classmethod
    def build(cls, components, bridge = None):
        bridge = bridge or cls()
        bridges = [bridge]
        for component in filter(bridge.is_connectable_with, components):
            bridges += cls.build(
                    filter(lambda x: x is not component, components),
                    bridge.append(component))
        return bridges


if __name__ == '__main__':
    components = [tuple(map(int, line.strip().split('/'))) for line in sys.stdin]
    bridges = Bridge.build(components)
    print('Maximum bridge strength is %d' % max(bridge.strength for bridge in bridges))
    print('Strength of the longest bridge is %d' % max(bridges).strength)
