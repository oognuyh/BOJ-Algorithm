"""
    15652. N과 M (4)
"""
from sys import stdin 
from itertools import combinations_with_replacement

N, M = map(int, stdin.readline().split())
for answer in map(' '.join, combinations_with_replacement(map(str, range(1, N + 1)), M)): print(answer)