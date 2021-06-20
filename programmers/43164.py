"""
    43164. 여행경로
"""
from collections import defaultdict, deque
from typing import List

def solution(tickets: List[str]) -> List[str]:
    routes = defaultdict(list)

    for takeoff, landing in tickets:
        routes[takeoff].append(landing)

    for takeoff in routes:
        routes[takeoff].sort(reverse = True)

    dq, path = deque(["ICN"]), []

    while dq:
        takeoff = dq[-1]
        if takeoff in routes and routes[takeoff]:
            dq.append(routes[takeoff].pop())
        else:
            path.append(dq.pop())

    return path[::-1]