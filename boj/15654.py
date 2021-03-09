"""
    15654. N과 M (5)
"""
from itertools import permutations

N, M = map(int, input().split())
targets = map(str, sorted(list(map(int, input().split()))))

print('\n'.join(map(' '.join, permutations(targets, M))))
