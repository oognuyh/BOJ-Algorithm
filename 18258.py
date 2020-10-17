"""
    18258. 큐 2
"""
from collections import deque
from sys import stdin

def do():
    for command in commands:
        if command == "front":
            print(q[0] if q else -1)

        elif command == "back":
            print(q[-1] if q else -1)

        elif command == "size":
            print(len(q))

        elif command == "empty":
            print(0 if q else 1)

        elif command == "pop":
            print(q.popleft() if q else -1)

        else:
            q.append(int(command.split()[1]))

if __name__ == "__main__":
    N = int(stdin.readline()) 
    # input 보다는 sys를 사용하자 하지만 개행이 포함되니 rstrip으로 제거 필요
    commands = [stdin.readline().rstrip() for _ in range(N)]
    q = deque()

    do()