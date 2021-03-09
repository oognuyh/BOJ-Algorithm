"""
    17298. 오큰수
"""
from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

def run(N, A):
    dq = deque([0])
    result = [-1 for _ in range(N)]

    for i in range(1, N):
        while dq and A[dq[-1]] < A[i]:
            result[dq[-1]] = A[i]
            dq.pop()
        
        dq.append(i)

    print(*result)

if __name__ == "__main__":
    run(int(read()), list(map(int, read().split())))