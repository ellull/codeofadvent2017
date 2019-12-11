#!/usr/bin/env python3
import fileinput
from itertools import permutations
from threading import Thread
from queue import Queue

class Intcode(Thread):
    def __init__(self, memory, input_queue, output_queue):
        super(Intcode, self).__init__()
        self.ic = 0
        self.memory = memory
        self.input_queue = input_queue
        self.output_queue = output_queue

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
                if params_addresses[0]:
                    next_ic = self.memory[params_addresses[1]]
            elif instruction == 6:
                next_ic, params_addresses = self._fetch_params_addresses(2, params_mode)
                if not params_addresses[0]:
                    next_ic = self.memory[params_addresses[1]]
            elif instruction == 7:
                next_ic, params_addresses = self._fetch_params_addresses(3, params_mode)
                self.memory[params_addresses[-1]] = 1 if self.memory[params_addresses[0]] < self.memory[params_addresses[1]] else 0
            elif instruction == 8:
                next_ic, params_addresses = self._fetch_params_addresses(3, params_mode)
                self.memory[params_addresses[-1]] = 1 if self.memory[params_addresses[0]] == self.memory[params_addresses[1]] else 0
            elif instruction == 99:
                return True

            self.ic = next_ic


class AmplificationCircuit(object):
    @staticmethod
    def __initQueue(phase_setting):
        queue = Queue(2)
        queue.put(phase_setting)
        return queue

    def __init__(self, program, phase_setting_sequence):
        queues = [AmplificationCircuit.__initQueue(phase_setting) for phase_setting in phase_setting_sequence]
        self.amplifiers = [Intcode(program[:], queues[i], queues[(i + 1) % len(queues)]) for i in range(len(queues))]

    def run(self):
        for amplifier in self.amplifiers:
            amplifier.start()

        self.amplifiers[0].input_queue.put(0)

        for amplifier in self.amplifiers:
            amplifier.join()
        
        return self.amplifiers[-1].output_queue.get()

if __name__ == "__main__":
    program = [int(value) for value in fileinput.input().readline().split(",")]

    max_thruster_signal = max(AmplificationCircuit(program, phase_setting_sequence).run() for phase_setting_sequence in permutations((0, 1, 2, 3, 4)))
    print("Max thruster signal: {:d}".format(max_thruster_signal))

    max_thruster_signal = max(AmplificationCircuit(program, phase_setting_sequence).run() for phase_setting_sequence in permutations((5, 6, 7, 8, 9)))
    print("Max thruster signal: {:d}".format(max_thruster_signal))
