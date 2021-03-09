"""
    1010. 다리 놓기
"""
from math import factorial
from sys import stdin

read = stdin.readline

def run(T):
    for _ in range(T):
        N, M = map(int, read().strip().split())        

        print(factorial(M) // (factorial(N) * factorial(M - N)))

if __name__ == "__main__":
    run(int(read().strip()))
