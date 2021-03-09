"""
    11049. 행렬 곱셈 순서
"""
from sys import stdin, maxsize
read = lambda : stdin.readline().strip()

def run(N):
    def get_matrices():
        return [list(map(int, read().split())) for _ in range(N)]
    
    matrices = get_matrices()
    DP = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(1, N):
        for j in range(N - i):
            DP[j][j + i] = maxsize
            for k in range(j, j + i):
                DP[j][j + i] = min(DP[j][j + i], DP[j][k] + DP[k + 1][j + i] + matrices[j][0] * matrices[k][1] * matrices[j + i][1])

    print(DP[0][-1])

if __name__ == "__main__":
    run(int(read()))