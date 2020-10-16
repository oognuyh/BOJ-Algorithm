"""
    2164. 카드2
"""
from collections import deque

def do():
    while len(q) > 1:
        q.popleft()
        top = q.popleft()
        q.append(top)

    print(q[0])

if __name__ == "__main__":
    N = int(input())
    q = deque(range(1, N + 1))
 
    do()