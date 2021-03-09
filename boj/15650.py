"""
    15650. N과 M (2)
"""
from itertools import combinations
from sys import stdin

N, M = map(int, stdin.readline().split())

for answer in map(' '.join, combinations(map(str, range(1, N + 1)), M)): print(answer)