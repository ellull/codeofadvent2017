#!/usr/bin/env python
import sys
from Queue import Queue, LifoQueue, Empty
from collections import defaultdict
from functools import partial
from threading import Thread

class Program(Thread):
    def __init__(self, instructions, a = 0):
        super(Program, self).__init__()
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.registers['a'] = a
        self.program_counter = 0
        self.muls = 0

        self.op = {
            'set': partial(self._apply, operation = lambda x, y: y),
            'sub': partial(self._apply, operation = lambda x, y: x - y),
            'mul': partial(self._apply, operation = lambda x, y: x * y),
            'jnz': self._jnz,
        }

    def _get(self, value):
        return self.registers[value] if value.isalpha() else int(value)

    def _apply(self, register, value, operation):
        self.registers[register] = operation(self.registers[register], self._get(value))

    def _jnz(self, register, offset):
        if self._get(register) != 0:
            return self._get(offset)

    def run(self):
        try:
            while self.program_counter < len(self.instructions):
                instruction = self.instructions[self.program_counter]
                if instruction[0] == 'mul':
                    self.muls += 1
                offset = self.op[instruction[0]](*instruction[1:])
                self.program_counter += 1 if offset is None else offset
        except Empty:
            print('[%d] Deadlock detected Exiting!!!' % self.id)

if __name__ == '__main__':
    instructions = tuple(tuple(line.strip().split(' ', 3)) for line in sys.stdin)

    p = Program(instructions)
    p.run()
    print("%d muls called" % p.muls)

    nonprimes = 0
    b = (84 * 100) + 100000
    for b in range(b, b + 17000 + 1, 17):
        if any(b % d == 0 for d in range(2, int(b**0.5))):
            nonprimes += 1
    print('h register value is %d' % nonprimes)
