#!/usr/bin/env python
import re
import sys

def dance_round(programs_str, dance_moves):
    programs = list(programs_str)

    for dance_move in dance_moves:
        if dance_move[0] == 's':
            split = int(dance_move[1:])
            programs = programs[-split:] + programs[:-split]
        elif dance_move[0] == 'x':
            a, b = (int(p) for p in dance_move[1:].split('/', 1))
            programs[a], programs[b] = programs[b], programs[a]
        elif dance_move[0] == 'p':
            a, b = programs.index(dance_move[1]), programs.index(dance_move[3])
            programs[a], programs[b] = programs[b], programs[a]

    return ''.join(programs)

def dance(programs, dance_moves, dances):
    seen = [programs]
    for num_dance in xrange(1, dances + 1):
        programs = dance_round(programs, dance_moves)
        if programs in seen:
            # If we detected a loop, we can skip all the loop iterations as these
            # number of iterations return the programs at the initial state.
            # Without this optimization, we would need ~282 days to loop throught the
            # 1000000000 iterations as requested instead of 2.5 seconds
            remainder = dances % (num_dance - seen.index(programs))
            return seen[remainder]
        seen.append(programs)
    return programs


if __name__ == '__main__':
    import time
    moves = next(sys.stdin).strip().split(',')
    programs = ''.join(chr(ord('a') + i) for i in xrange(16))
    print('Programs order after first dance: %s' % dance(programs, moves, 1))
    print('Programs order after 1.000.000.000 dances: %s' % dance(programs, moves, 1000000000))

