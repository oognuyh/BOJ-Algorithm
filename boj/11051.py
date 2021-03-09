"""
    11051. 이항 계수 2
"""
from math import factorial

N, K = map(int, input().split())
# factiorial 함수가 제공되는 것을 오늘 알았다.
print((factorial(N) // (factorial(K) * factorial(N - K))) % 10007)
