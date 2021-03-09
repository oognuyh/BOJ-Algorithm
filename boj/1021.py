"""
    1021. 회전하는 큐
"""
from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().strip().split())
targets = deque(map(int, stdin.readline().strip().split()))

numbers = deque(range(1, N + 1))
count = 0

while targets:
    target = targets.popleft()

    while True:
        if target == numbers[0]: # method 1
            numbers.popleft()
            break
        else: # method 2, 3
            if numbers.index(target) > len(numbers) // 2: # method 3
                number = numbers.pop()
                numbers.appendleft(number)
            else: # method 2
                number = numbers.popleft()
                numbers.append(number)

            count += 1

print(count)