"""
    9375. 패션왕 신해빈
"""
from collections import Counter

N = int(input())

cases = [[input().split()[-1] for _ in range(int(input()))] for _ in range(N)]

for case in cases:
    clothes = Counter(case)
    total = 1
    for value in map(lambda x : x + 1, clothes.values()): total *= value
    print(total - 1)