"""
    11444. 피보나치 수 6
"""
from sys import stdin

MOD = 1000000007

def run(N):
    def multiply(A, B):
        return [[sum([_a * _b for _a, _b in zip(a, b)]) % MOD for b in zip(*B)] for a in A]

    V = [[1, 1], [1, 0]]
    F = [[1, 0], [0, 1]]

    while N > 0:
        if N % 2 == 1:
            F = multiply(F, V)
        V = multiply(V, V)
        N //= 2

    print(F[0][1])

if __name__ == "__main__":
    run(int(stdin.readline().strip()))