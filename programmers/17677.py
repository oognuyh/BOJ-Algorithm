"""
    17677. [1차] 뉴스 클러스터링
"""
from collections import Counter
from typing import List

def solution(str1: str, str2: str) -> int:
    def get_elements(string: str) -> List[str]:
        return [string[i:i + 2] for i in range(len(string) - 1) if string[i:i + 2].isalpha()]

    A = Counter(get_elements(str1.lower()))
    B = Counter(get_elements(str2.lower()))

    intersection, union = len(list((A & B).elements())), len(list((A | B).elements()))

    J = intersection / union if union > 0 else 1

    return int(J * 65536)