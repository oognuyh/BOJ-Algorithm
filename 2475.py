"""
    2475. 검증수
"""
from sys import stdin

numbers = map(int, stdin.readline().strip().split())
numbers = map(lambda number: number ** 2, numbers)

print(sum(numbers) % 10)
