from itertools import product

def difference(iterable):
    return max(iterable) - min(iterable)

def divisible(iterable):
    return sum(x / y if x % y == 0 and x != y else 0 for (x, y) in product(iterable, repeat=2))

def solve(puzzle, function):
    return sum(function(row) for row in puzzle)
