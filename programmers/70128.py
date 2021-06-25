"""
    70128. 내적
"""
from typing import List

def solution(a: List[int], b: List[int]) -> int:
    return sum([_a * _b for _a, _b in zip(a, b)])