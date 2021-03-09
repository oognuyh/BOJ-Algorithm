"""
    9251. LCS
"""
from sys import stdin

def run(s1, s2):
    def create_matrix():
        return [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

    dp = create_matrix()

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i - 1][j - 1] + 1 if s1[j - 1] == s2[i - 1] else max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])

if __name__ == "__main__":
    strings = [stdin.readline().strip() for _ in range(2)]
    
    run(*strings)