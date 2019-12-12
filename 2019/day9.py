#!/usr/bin/env python3
import fileinput
from collections import defaultdict
from threading import Thread
from queue import Queue

class Memory(defaultdict):
    def __init__(self, content):
        super(Memory, self).__init__(int, enumerate(content))

    def __getitem__(self, address):
        if address < 0:
            raise KeyError("address must be greather than or equal to 0")
        return super(Memory, self).__getitem__(address)

    def __setitem__(self, address, value):
        if address < 0:
            raise KeyError("address must be greather than or equal to 0")
        return super(Memory, self).__setitem__(address, value)


class Intcode(Thread):
    def __init__(self, program, input_queue = None, output_queue = None):
        super(Intcode, self).__init__()
        self.ic = 0
        self.relative_base = 0
        self.memory = Memory(program)
        self.input_queue = input_queue if input_queue is not None else Queue()
        self.output_queue = output_queue if output_queue is not None else Queue()

    def _fetch_instruction(self):
        opcode = self.memory[self.ic]
        return (opcode % 100, opcode // 100)
    
    def _fetch_params_addresses(self, num_params, params_mode):
            params_addresses = []
            modes = [int(mode) for mode in "{:03d}".format(params_mode)]
            for i in range(num_params):
                mode = modes.pop()
                param_address = self.ic + i + 1
                if mode == 0:
                    param_address = self.memory[param_address]
                if mode == 2:
                    param_address = self.memory[param_address] + self.relative_base
                params_addresses.append(param_address)
            return self.ic + num_params + 1, tuple(params_addresses)

    def run(self):
        while True:
            instruction, params_mode = self._fetch_instruction()
            if instruction == 1:
                next_ic, params_addresses = self._fetch_params_addresses(3, params_mode)
                self.memory[params_addresses[2]] = self.memory[params_addresses[0]] + self.memory[params_addresses[1]]
            elif instruction == 2:
                next_ic, params_addresses = self._fetch_params_addresses(3, params_mode)
                self.memory[params_addresses[2]] = self.memory[params_addresses[0]] * self.memory[params_addresses[1]]
            elif instruction == 3:
                next_ic, params_addresses = self._fetch_params_addresses(1, params_mode)
                self.memory[params_addresses[0]] = self.input_queue.get()
            elif instruction == 4:
                next_ic, params_addresses = self._fetch_params_addresses(1, params_mode)
                self.output_queue.put(self.memory[params_addresses[0]])
            elif instruction == 5:
                next_ic, params_addresses = self._fetch_params_addresses(2, params_mode)
                if self.memory[params_addresses[0]]:
                    next_ic = self.memory[params_addresses[1]]
            elif instruction == 6:
                next_ic, params_addresses = self._fetch_params_addresses(2, params_mode)
                if not self.memory[params_addresses[0]]:
                    next_ic = self.memory[params_addresses[1]]
            elif instruction == 7:
                next_ic, params_addresses = self._fetch_params_addresses(3, params_mode)
                self.memory[params_addresses[-1]] = 1 if self.memory[params_addresses[0]] < self.memory[params_addresses[1]] else 0
            elif instruction == 8:
                next_ic, params_addresses = self._fetch_params_addresses(3, params_mode)
                self.memory[params_addresses[-1]] = 1 if self.memory[params_addresses[0]] == self.memory[params_addresses[1]] else 0
            elif instruction == 9:
                next_ic, params_addresses = self._fetch_params_addresses(1, params_mode)
                self.relative_base += self.memory[params_addresses[0]]
            elif instruction == 99:
                break

            self.ic = next_ic
        
        return self

computer = Intcode([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]).run()
assert list(computer.output_queue.queue) == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]

computer = Intcode([1102, 34915192, 34915192, 7, 4, 7, 99, 0]).run()
assert len(str(computer.output_queue.get())) == 16

computer = Intcode([104, 1125899906842624, 99]).run()
assert computer.output_queue.get() == 1125899906842624

class SingleQueue(object):
    def __init__(self, value):
        self._value = value
        self._used = False
    
    def get(self):
        if self._used:
            raise Exception
        self._used = True
        return self._value

if __name__ == "__main__":
    program = [int(value) for value in fileinput.input().readline().split(",")]

    print("BOOST keycode = {:d}".format(Intcode(program, SingleQueue(1)).run().output_queue.get()))

    print("Coordinates = {:d}".format(Intcode(program, SingleQueue(2)).run().output_queue.get()))
