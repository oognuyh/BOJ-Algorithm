"""
    42842. 카펫
"""
from typing import List 
from math import sqrt

def solution(brown: int, yellow: int) -> List[int]:
    for row in range(1, int(sqrt(yellow)) + 1):
        if yellow % row == 0:
            column = yellow // row 
            if row * 2 + 2 * column + 4 == brown:
                return [column + 2, row + 2]
"""
    # Others
        1. Quadratic formula
            import math

            def solution(brown, yellow):
                w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
                h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
                return [w,h]

        2. brown + yellow
            def solution(brown, yellow):
                s = brown + yellow
                for i in range(s, 2, -1):
                    if s % i == 0:
                        a = s // i
                        if yellow == (i - 2) * (a - 2):
                            return [i, a]
"""
