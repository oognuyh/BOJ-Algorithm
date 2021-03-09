"""
    11066. 파일 합치기
    ref : https://data-make.tistory.com/402
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(T):
    def get_file_sizes():
        return int(read()), [0] + list(map(int, read().split()))

    def get_cumulative_sum():
        return [sum(file_sizes[:i + 1]) for i in range(K + 1)]

    for _ in range(T):
        K, file_sizes = get_file_sizes()
        cumulative_sum = get_cumulative_sum()

        DP = [[0 for _ in range(K + 1)] for _ in range(K + 1)]
    
        for i in range(2, K + 1):
            for j in range(1, K + 2 - i):
                DP[j][j + i - 1] = min([DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]) + cumulative_sum[j + i - 1] - cumulative_sum[j - 1]

        print(DP[1][-1])

if __name__ == "__main__":
    run(int(read()))