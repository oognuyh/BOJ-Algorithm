"""
    1912. 연속합
"""
from sys import stdin 

def run():
    dp = [0 for _ in range(N)]
    dp[0], maximum = numbers[0], numbers[0]

    for i in range(1, N):
        dp[i] = max(dp[i - 1] + numbers[i], numbers[i])
        maximum = max(dp[i], maximum)
    
    print(maximum)

if __name__ == "__main__":
    N = int(stdin.readline().strip())
    numbers = list(map(int, stdin.readline().strip().split()))

    run()