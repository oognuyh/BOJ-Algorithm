"""
    2740. 행렬 곱셈
"""
from sys import stdin

def multiply(A, B):
    return [[sum([_a * _b for _a, _b in zip(a, b)]) for b in B] for a in A]

if __name__ == "__main__":
    N, M = map(int, stdin.readline().strip().split()) # 행렬 A의 크기 N, M
    A = [list(map(int, stdin.readline().strip().split())) for _ in range(N)] # N개의 줄에 A의 원소 M개
    
    M, K = map(int, stdin.readline().strip().split()) # 행렬 B의 크기 M, K
    B = [list(map(int, stdin.readline().strip().split())) for _ in range(M)] # M개의 줄에 B의 원소 K개
    B = list(map(list, zip(*B)))

    for row in multiply(A, B):
        for element in row:
            print(element, end = " ")
        print("")