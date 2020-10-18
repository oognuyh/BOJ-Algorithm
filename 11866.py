"""
    11866. 요세푸스 문제 0
"""
from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N + 1))

print("<", end = "")
while people:
    for _ in range(K - 1):
        element = people.popleft()
        people.append(element)
    print(str(people.popleft()) + ", " if len(people) > 1 else str(people.popleft()), end = "")
print(">")