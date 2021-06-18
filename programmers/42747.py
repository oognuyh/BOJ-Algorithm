"""
    42747. H-Index
"""
from typing import List

def solution(citations: List[int]) -> int:
    for i, citation in enumerate(sorted(citations)):
        if citation >= len(citations) - i:
            return len(citations) - i
    
    return 0

"""
    # Others
        1. enumerate
            def solution(citations):
                citations.sort(reverse = True)
                return max(map(min, enumerate(citations, start = 1)))
"""