#!/usr/bin/env python
import re
import sys
from itertools import count, dropwhile

class Scanner(object):
    def __init__(self, n):
        self.range = n
        self.period = 2 * (n - 1)

    def _cycle(self, n):
        i = n % self.period
        return i if i < self.range else self.period - i

    def __getitem__(self, index):
        return self._cycle(index)

    def __repr__(self):
        return 'Scanner(%d)' % self.range

class Firewall(object):
    _exhausted = object()

    def __init__(self, configuration):
        self.scanners = {int(layer): Scanner(int(depth)) for (layer, depth) in configuration}

    def scores(self, delay):
        return (depth * scanner.range for (depth, scanner) in self.scanners.iteritems() if scanner[depth + delay] == 0)

    def severity(self, delay):
        return sum(self.scores(delay))

    def caught(self, delay):
        return next(self.scores(delay), Firewall._exhausted) != Firewall._exhausted

    def details(self, delay):
        return {depth: scanner[depth + delay] for (depth, scanner) in self.scanners.iteritems()}

if __name__ == '__main__':
    firewall = Firewall(line.strip().split(": ") for line in sys.stdin)
    print('Severity: %d' % firewall.severity(0))
    print('Packet delay to pass through the firewall: %d picoseconds' % next(dropwhile(firewall.caught, count(10))))
    
