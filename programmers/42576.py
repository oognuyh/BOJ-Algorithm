"""
    42576. 완주하지 못한 선수
"""
from collections import Counter
from typing import List

def solution(participant: List[str], completion: List[str]) -> str:
    return (Counter(participant) - Counter(completion)).popitem()[0]