#!/usr/bin/env python3
import fileinput
import math
from typing import List, Tuple


class Intcode(object):
    class Instruction(object):
        def __init__(self, num_input_params, num_output_params, is_jump, code):
            self.num_input_params = num_input_params
            self.num_output_params = num_output_params
            self.is_jump = is_jump
            self.code = code

        @property
        def num_params(self):
            return self.num_input_params + self.num_output_params

        def execute(self, params_mode, intcode):
            input_params = self._fetch_input_params(params_mode, intcode)
            result = self.code(*input_params)

            if self.is_jump:
                intcode.ic = result if result is not None else intcode.ic + self.num_params + 1
                return

            if self.num_output_params:
                output_position = intcode.memory[intcode.ic + self.num_input_params + 1]
                intcode.memory[output_position] = result
            intcode.ic += self.num_params + 1

        def _fetch_input_params(self, params_mode, intcode) -> Tuple[int]:
            input_params = []
            for i in range(self.num_input_params):
                mode = (params_mode // int(math.pow(10, i))) % 10
                if mode == 0:
                    address = intcode.memory[intcode.ic + i + 1]
                elif mode == 1:
                    address = intcode.ic + i + 1
                param = intcode.memory[address]
                input_params.append(param)            
            return tuple(input_params)


    __instructions = {
        1: Instruction(2, 1, False, lambda x, y: x + y),
        2: Instruction(2, 1, False, lambda x, y: x * y),
        3: Instruction(0, 1, False, lambda: int(input("Input: "))),
        4: Instruction(1, 0, False, lambda x: print("Output: {:d}".format(x))),
        5: Instruction(2, 0, True, lambda v, i: i if v else None),
        6: Instruction(2, 0, True, lambda v, i: i if not v else None),
        7: Instruction(2, 1, False, lambda x, y: 1 if x < y else 0),
        8: Instruction(2, 1, False, lambda x, y: 1 if x == y else 0),
    }

    def __init__(self, memory):
        self.ic = 0
        self.memory = memory


    def fetch(self):
        opcode = self.memory[self.ic]
        return (opcode % 100, opcode // 100)
    
    def run(self):
        while True:
            instruction, params_mode = self.fetch()
            if instruction == 99:
                return True
            Intcode.__instructions[instruction].execute(params_mode, self)

if __name__ == "__main__":
    intcode = Intcode([int(opcode) for opcode in fileinput.input().readline().split(",")])
    success = intcode.run()
