"""
    10844. 쉬운 계단 수
"""
N = int(input())

dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1] for _ in range(101)] 

for i in range(2, N + 1):
    for j in range(0, 10):
        dp[i][j] = dp[i - 1][j - 1] if j == 9 else dp[i - 1][j + 1] if j == 0 else dp[i - 1][j - 1] + dp[i - 1][j + 1] 
        
print(sum(dp[N]) % 1000000000)