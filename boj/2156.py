"""
    2156. 포도주 시식
"""
N = int(input())
amounts = [0] + [int(input()) for _ in range(N)]
dp = [0 for _ in range(N + 1)]
if N == 1: 
    print(amounts[1])
else:
    dp[1] = amounts[1]; dp[2] = amounts[1] + amounts[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + amounts[i - 1] + amounts[i], dp[i - 1], dp[i - 2] + amounts[i])
    print(dp[N])    