#!/usr/bin/env python

LEFT = -1
RIGHT = 1

class Action(object):
    def __init__(self, write, move, next_state):
        self.write = write
        self.move = move
        self.next_state = next_state


class TouringMachine(object):
    def __init__(self, states, tape):
        self.steps = 0
        self.states = states
        self.tape = tape
        self.position = 0
        self.current_state = 'A'

    def step(self):
        self.steps += 1
        action = self.states[self.current_state][self.tape.get(self.position, False)]
        self.tape[self.position] = action.write
        self.position += action.move
        self.current_state = action.next_state


if __name__ == '__main__':
    steps = 12399302
    states = {
            'A': {False: Action(True, RIGHT, 'B'), True: Action(False, RIGHT, 'C')},
            'B': {False: Action(False, LEFT, 'A'), True: Action(False, RIGHT, 'D')},
            'C': {False: Action(True, RIGHT, 'D'), True: Action(True, RIGHT, 'A')},
            'D': {False: Action(True, LEFT, 'E'), True: Action(False, LEFT, 'D')},
            'E': {False: Action(True, RIGHT, 'F'), True: Action(True, LEFT, 'B')},
            'F': {False: Action(True, RIGHT, 'A'), True: Action(True, RIGHT, 'E')},
            }

    tape = {}
    touring_machine = TouringMachine(states, tape)
    for step in xrange(steps):
        print('%08d: %s %s %s' % (step, touring_machine.current_state, touring_machine.position, tape.get(touring_machine.position, False)))
        touring_machine.step()

    print('Diagnostic checksum after %d steps is %d' % (steps, sum(tape.itervalues())))

