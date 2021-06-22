"""
    77484. 로또의 최고 순위와 최저 순위
"""
from typing import List
from collections import Counter

def solution(lottos: List[int], win_nums: List[int]) -> List[int]:
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    correct_answers = Counter(lottos) & Counter(win_nums)

    return [rank[len(correct_answers) + lottos.count(0)], rank[len(correct_answers)]]

"""
    # Others
        1. set
            def solution(lottos, win_nums):
                rank = {
                    0: 6,
                    1: 6,
                    2: 5,
                    3: 4,
                    4: 3,
                    5: 2,
                    6: 1
                }
                
                return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
"""