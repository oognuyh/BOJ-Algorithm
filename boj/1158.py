"""
    1158. 요세푸스 문제
"""
from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

def run(N, K):
    def get_kth_person():
        for _ in range(K - 1):
            persons.append(persons.popleft())
        return persons.popleft()

    persons, result = deque(range(1, N + 1)), []

    while persons:
        result += [get_kth_person()]

    print(f"<{', '.join(map(str, result))}>")

if __name__ == "__main__":
    run(*map(int, read().split()))