"""
    1149. RGB 거리
"""
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[costs[0][color] for _ in range(N)] for color in range(3)]

for i in range(1, N):
    dp[0][i] = costs[i][0] + min(dp[1][i - 1], dp[2][i - 1])
    dp[1][i] = costs[i][1] + min(dp[0][i - 1], dp[2][i - 1])
    dp[2][i] = costs[i][2] + min(dp[0][i - 1], dp[1][i - 1])

print(min([dp[color][-1] for color in range(3)]))