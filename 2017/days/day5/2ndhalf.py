#!/usr/bin/env python
import fileinput

jumps = [int(jump) for jump in fileinput.input()]

clock, pc, max_pc = 0, 0, 0
while 0 <= pc < len(jumps):
    jump = jumps[pc]
    jumps[pc] += (1 if jump < 3 else -1)
    pc += jump
    clock += 1
    if pc > max_pc:
        max_pc = pc
        print("%09d: %04d" % (clock, pc))

print(clock)
