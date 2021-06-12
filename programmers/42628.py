"""
    42628. 이중우선순위큐
"""
from typing import List
import heapq

def solution(operations: List[str]) -> List[int]:
    hq = []

    while operations:
        operation = operations.pop(0)
        command, value = operation.split()

        if command == "I":
            heapq.heappush(hq, int(value))
        else:
            if hq:
                if value == "1":
                    hq.pop(-1)
                else:
                    heapq.heappop(hq)

    return [max(hq), hq[0]] if hq else [0, 0]