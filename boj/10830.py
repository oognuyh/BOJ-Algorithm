"""
    10830. 행렬 제곱
"""
from sys import stdin

def product(a, b):
    return [[sum([(a[y][i] * b[i][x]) for i in range(N)]) % 1000 for x in range(N)] for y in range(N)]

def divide(a, n):
    if n == 1:
        return a
    elif n == 2:
        return product(a, a)

    if n % 2 == 0:
        a = divide(a, n // 2)
        return product(a, a) 
    else:
        return product(divide(a, n - 1), a)

if __name__ == "__main__":
    N, B = map(int, stdin.readline().strip().split())
    A = [list(map(lambda element: int(element) % 1000, stdin.readline().strip().split())) for _ in range(N)]
    # B가 1일 수도 있으므로 받자마자 처리

    for row in divide(A, B):
        print(*row, sep = " ")