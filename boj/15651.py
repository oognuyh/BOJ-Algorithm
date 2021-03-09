"""
    15651. N과 M (3)
"""
from sys import stdin 
from itertools import product

N, M = map(int, stdin.readline().split())

for answer in map(' '.join, product(''.join(map(str, range(1, N + 1))), repeat = M)): print(answer)