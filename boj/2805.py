"""
    2805. 나무 자르기
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(N, M, trees):
    def get_felled_height():
        return sum([tree - mid for tree in trees if tree > mid])

    start, end = 0, max(trees)

    while start <= end:
        mid = (start + end) // 2

        if get_felled_height() >= M:
            start = mid + 1
        else:
            end = mid - 1
    
    print(end)

if __name__ == "__main__":
    run(*map(int, read().split()), list(map(int, read().split())))