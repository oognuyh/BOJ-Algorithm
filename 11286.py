"""
    11286. 절댓값 힙
"""
from sys import stdin
import heapq

q = []

def run(operator):
    if operator == 0:
        print(0 if not q else heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(operator), operator))

if __name__ == "__main__":
    N = int(stdin.readline().strip())

    for _ in range(N):
        operator = int(stdin.readline().strip())
        run(operator)