#!/usr/bin/env python
import sys
from itertools import imap, izip, islice, ifilter

def generator(seed, factor):
    prev = seed
    while True:
        prev = (prev * factor) % 2147483647
        yield prev

def last_bits(bits):
    mask = sum(1 << shift for shift in xrange(bits))
    return lambda n: n & mask

duel1 = izip(
        imap(last_bits(16), generator(int(sys.argv[1]), 16807)),
        imap(last_bits(16), generator(int(sys.argv[2]), 48271)))
#print(sum(a ==  b for (a, b) in islice(duel1, 40000000)))

duel2 = izip(
        imap(last_bits(16), ifilter(lambda x: x % 4 == 0, generator(int(sys.argv[1]), 16807))),
        imap(last_bits(16), ifilter(lambda x: x % 8 == 0, generator(int(sys.argv[2]), 48271))))
print(sum(a ==  b for (a, b) in islice(duel2, 5000000)))
