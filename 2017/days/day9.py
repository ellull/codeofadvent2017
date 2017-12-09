#!/usr/bin/env python
import sys

def skip_garbage(iterable):
    count = 0
    for char in iterable:
        # Found end of garbage
        if char == '>':
            break
        # Found skip character
        if char == '!':
            next(iterable)  # Skip next character
        else:
            # Count the ammount of garbage
            count += 1

    # Return the amount of garbage
    return count

def parse(iterable):
    depth, score, garbage = 0, 0, 0

    for char in iterable:
        # Found start of garbage
        if char == '<':
            # Skip garbage and accumulate the amount of garbage
            garbage += skip_garbage(iterable)

        # Found start of group
        if char == '{':
            depth += 1      # Increment the depth
            score += depth  # Accumulate the score
        # Found end of group
        if char == '}':
            depth -= 1      # Decrement the depth

    return (score, garbage)

if __name__ == '__main__':
    score = parse(iter(next(sys.stdin)))
    print("Score: %d" % score[0])
    print("Garbage: %d" % score[1])
