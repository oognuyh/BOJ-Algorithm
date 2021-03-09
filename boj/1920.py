"""
    1920. 수 찾기
"""
from bisect import bisect_left
from sys import stdin

def find(x):
    def is_in_a():
        index = bisect_left(A, x)
        return True if index < len(A) and A[index] == x else False
        # 연속된 수만 생각해서 1차 실패
        # A[index]가 x 인지 확인해야 포함되는지 알 수 있음

    print(1 if is_in_a() else 0)

if __name__ == "__main__":
    N = int(stdin.readline().strip())
    A = sorted(map(int, stdin.readline().strip().split()))
    M = int(stdin.readline().strip())
    X = map(int, stdin.readline().strip().split())

    for x in X:
        find(x)