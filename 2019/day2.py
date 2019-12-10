#!/usr/bin/env python3
import fileinput

opcodes = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y
}


def execute(integers):
    pc = 0
    try:
        while True:
            opcode = integers[pc]
            if opcode == 99:
                break
            input1_pos, input2_pos, output_pos = integers[pc+1:pc+4]
            integers[output_pos] = opcodes.get(opcode)(integers[input1_pos], integers[input2_pos])
            pc += 4
    except TypeError:
        print("Got an unexpected opcode {:d}".format(opcode))
    return integers


if __name__ == '__main__':
    from itertools import product

    assert execute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert execute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert execute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert execute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert execute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    input = [int(value) for value in fileinput.input().readline().split(",")]

    # First half
    program_alarm = input[:]
    program_alarm[1:3] = [12, 2]
    print("Position 0 = {:d}".format(execute(program_alarm)[0]))

    # Second half
    for (noun, verb) in product(range(100), range(100)):
        program = input[:]
        program[1:3] = [noun, verb]
        if execute(program)[0] == 19690720:
            print("Result = {:d}".format(noun * 100 + verb))
            break
