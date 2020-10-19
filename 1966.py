"""
    1966. 프린터 큐
"""
from collections import deque

test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    documents = deque(range(N))

    while documents:
        document = documents.popleft()

        if priorities[document] == max(priorities):
            priorities[document] = -1

            if document == M:
                print(N - len(documents))
                break
        else:
            documents.append(document)