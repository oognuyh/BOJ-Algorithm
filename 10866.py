"""
    10866. 덱
"""
from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
commands = [stdin.readline().strip().split() for _ in range(N)]
deq = deque()

for command in commands:
    if command[0] == "push_back":
        deq.append(int(command[1]))
    elif command[0] == "push_front":
        deq.appendleft(int(command[1]))
    elif command[0] == "front":
        print(deq[0] if deq else -1)
    elif command[0] == "back":
        print(deq[-1] if deq else -1)
    elif command[0] == "empty":
        print(0 if deq else 1)
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "pop_front":
        print(deq.popleft() if deq else -1)
    elif command[0] == "pop_back":
        print(deq.pop() if deq else -1)