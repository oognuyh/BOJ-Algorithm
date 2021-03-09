"""
    1676. 팩토리얼 0의 개수
"""
from math import factorial

N = int(input())
value, count = factorial(N), 0
while value % 10 == 0:
    value //= 10; count += 1
print(count)