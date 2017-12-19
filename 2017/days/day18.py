#!/usr/bin/env python
import sys
from Queue import Queue, LifoQueue, Empty
from collections import defaultdict
from functools import partial
from threading import Thread

class Program(Thread):
    def __init__(self, pid, instructions, input_queue, output_queue):
        super(Program, self).__init__()
        self.id = pid
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.program_counter = 0
        self.registers['p'] = pid
        self.sent = 0

        self.op = {
            'snd': self._snd,
            'set': partial(self._apply, operation = lambda x, y: y),
            'add': partial(self._apply, operation = lambda x, y: x + y),
            'mul': partial(self._apply, operation = lambda x, y: x * y),
            'mod': partial(self._apply, operation = lambda x, y: x % y),
            'rcv': self._rcv,
            'jgz': self._jgz,
        }

    def _get(self, value):
        return self.registers[value] if value.isalpha() else int(value)

    def _apply(self, register, value, operation):
        self.registers[register] = operation(self.registers[register], self._get(value))

    def _snd(self, value):
        self.sent += 1
        self.output_queue.put(self._get(value))

    def _rcv(self, value):
        self.registers[value] = self.input_queue.get(True, 1)

    def _jgz(self, register, offset):
        if self._get(register) > 0:
            return self._get(offset)

    def run(self):
        try:
            while self.program_counter < len(self.instructions):
                instruction = self.instructions[self.program_counter]
                offset = self.op[instruction[0]](*instruction[1:])
                self.program_counter += 1 if offset is None else offset
        except Empty:
            print('[%d] Deadlock detected Exiting!!!' % self.id)

class SingletonQueue(object):
    def __init__(self):
        self.value = None

    def put(self, value):
        self.value = value

    def get(self, block = False, timeout = 0):
        raise Empty

if __name__ == '__main__':
    instructions = tuple(tuple(line.strip().split(' ', 3)) for line in sys.stdin)

    queue = SingletonQueue()
    p = Program(0, instructions, queue, queue)
    p.start()
    p.join()
    print("First rcv value: %d" % queue.value)

    q01, q10 = Queue(), Queue()
    p0, p1 = Program(0, instructions, q10, q01), Program(1, instructions, q01, q10)
    p0.start()
    p1.start()
    p0.join()
    p1.join()

    print('Program 1 sent %d values' % p1.sent)
