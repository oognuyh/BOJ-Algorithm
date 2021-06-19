"""
    43163. 단어 변환
"""
from typing import List
from collections import Counter

def solution(begin: str, target: str, words: List[str]) -> int:
    def transform(word: str, visited: List[str]):
        if word == target:
            steps.append(len(visited))
            return

        for candidate in words:
            if candidate not in visited:
                if len(Counter(candidate) - Counter(word)) <= 1:
                    transform(candidate, visited + [candidate])

    if target not in words: return 0
    
    steps = []
    
    transform(begin, [])

    return min(steps)