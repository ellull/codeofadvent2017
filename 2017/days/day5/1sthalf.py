#!/usr/bin/env python
import fileinput

jumps = [int(jump) for jump in fileinput.input()]

clock, pc = 0, 0
while pc < len(jumps):
    jump = jumps[pc]
    jumps[pc] += 1
    pc += jump
    clock += 1

print(clock)
