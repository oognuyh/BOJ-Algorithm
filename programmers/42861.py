"""
    42861. 섬 연결하기
"""
from typing import List

def solution(n: int, costs: List[List[str]]) -> int:
    costs = sorted(costs, key = lambda cost: cost[2])
    visited = [True] + [False for _ in range(n - 1)]
    answer = 0
    
    while not all(visited):
        for src, dest, cost in costs:
            if visited[src] and visited[dest]: continue

            if visited[src] or visited[dest]:
                visited[src] = visited[dest] = True
                answer += cost
                break

    return answer