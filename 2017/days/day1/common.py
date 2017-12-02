from itertools import tee, izip, chain 

def pairwise(iterable, n): 
   "s -> (s0,s1), (s1,s2), (s2, s3), ..., (sn, s0)" 
   a, b = tee(iterable) 
   tail = [next(b, None) for i in range(n)]
   return izip(a, chain(b, tail)) 

def solve(puzzle, n):
    if n < 1:
        raise ValueError("n must be greather or equal to 1")
    return sum(int(x) if x == y else 0 for (x, y) in pairwise(puzzle, n))
