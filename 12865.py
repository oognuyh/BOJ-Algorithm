"""
    12865. 평범한 배낭
"""
from sys import stdin

def run():
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight, value = things[i]
            
            dp[i][j] = dp[i - 1][j] if j < weight else max(value + dp[i - 1][j - weight], dp[i - 1][j])
            
    print(dp[-1][-1])

if __name__ == "__main__":
    N, K = map(int, stdin.readline().strip().split()) # 물품의 수, 버틸 수 있는 무게
    things = [[0, 0]] + [list(map(int, stdin.readline().strip().split())) for _ in range(N)]

    run()