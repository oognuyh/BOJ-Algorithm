"""
    42895. N으로 표현
"""
from collections import defaultdict

def solution(N: int, number: int) -> int:
    dp = defaultdict(set)

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    dp[i].add(k + l)
                    dp[i].add(k - l)
                    dp[i].add(k * l)
                    dp[i].add(k // l) if l != 0 else False

        if number in dp[i]: return i

    return -1