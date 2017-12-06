#!/usr/bin/env python
import fileinput

jumps = [int(jump) for jump in fileinput.input()]

clock, pc = 0, 0
while 0 <= pc < len(jumps):
    jump = jumps[pc]
    jumps[pc] += (1 if jump < 3 else -1)
    pc += jump
    clock += 1
    print("%09d -> %04d : %04d (%04d)" % (clock, jump, pc, jump + (1 if jump < 3 else -1)))

print(clock)
