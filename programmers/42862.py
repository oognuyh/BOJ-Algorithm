"""
    42862. 체육복
"""
from typing import List

def solution(n: int, lost: List[str], reserve: List[str]) -> int:
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))

    for reserver in reserve: 
        if reserver - 1 in lost:
            lost.remove(reserver - 1)
        elif reserver + 1 in lost: 
            lost.remove(reserver + 1)

    return n - len(lost)