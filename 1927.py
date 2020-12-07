"""
    1927. 최소 힙
"""
from sys import stdin 
import heapq 

q = []

def run(x):
    if x == 0: # pop
        print(heapq.heappop(q) if q else 0)
    else: # push
        heapq.heappush(q, x)

if __name__ == "__main__":
    N = int(stdin.readline().strip())

    for _ in range(N):
        run(int(stdin.readline().strip()))