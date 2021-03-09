"""
    2565. 전깃줄
"""
from sys import stdin

N = int(stdin.readline().strip())
# if want to sort, map object must be converted to list
lines = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]; lines.sort()
dp = [1 for _ in range(N)]

for i in range(1, N):
    try:
        dp[i] = max([dp[j] for j in range(i) if lines[j][1] < lines[i][1]]) + 1
    except:
        pass

print(N - max(dp))