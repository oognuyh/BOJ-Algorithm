"""
    1654. 랜선 자르기
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(K, N):
    def get_lans():
        return [int(read()) for _ in range(K)]

    def get_count_lan_cut():
        return sum([lan // mid for lan in lans])

    lans = get_lans()
    start, end = 1, max(lans)

    while start <= end:
        mid = (start + end) // 2

        count_lan_cut = get_count_lan_cut()

        if count_lan_cut < N:
            end = mid - 1
        else:
            start = mid + 1

    print(end)

if __name__ == "__main__":
    run(*map(int, read().split()))