#!/usr/bin/env python
import sys

def reallocate(banks):
    reallocate_blocks = max(banks)
    reallocate_bank = banks.index(reallocate_blocks)
    new_banks = list(banks)
    new_banks[reallocate_bank] = 0
    for i in range(reallocate_blocks):
        new_banks[(reallocate_bank + i + 1) % len(banks)] += 1
    return tuple(new_banks) 

seen, banks = dict(), tuple(int(blocks) for blocks in sys.argv[1].split(" "))
print("With initial block counts: %s" % str(banks))

while banks not in seen:
    seen[banks] = len(seen) + 1
    banks = reallocate(banks)

print("Redistribution cicles until loop: %d" % len(seen))
print("Loop length: %d" % (len(seen) - seen[banks] + 1))
