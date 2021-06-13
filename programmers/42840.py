"""
    42840. 모의고사
"""
from typing import List

def solution(answers: List[int]) -> List[int]:
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        if answer == a[i % len(a)]:
            scores[0] += 1
        if answer == b[i % len(b)]:
            scores[1] += 1
        if answer == c[i % len(c)]:
            scores[2] += 1

    return [i + 1 for i, score in enumerate(scores) if max(scores) == score]

"""
    # Others
        1. cycle
            from itertools import cycle

            def solution(answers):
                giveups = [
                    cycle([1,2,3,4,5]),
                    cycle([2,1,2,3,2,4,2,5]),
                    cycle([3,3,1,1,2,2,4,4,5,5]),
                ]
                scores = [0, 0, 0]
                for num in answers:
                    for i in range(3):
                        if next(giveups[i]) == num:
                            scores[i] += 1
                highest = max(scores)

                return [i + 1 for i, v in enumerate(scores) if v == highest]
"""