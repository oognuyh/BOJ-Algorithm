"""
    42885. 구명보트
"""
from collections import deque
from typing import List

def solution(people: List[int], limit: int) -> int:
    people, num_of_boats = deque(sorted(people)), 0

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.popleft()
        people.pop()

        num_of_boats += 1

    return num_of_boats if not people else num_of_boats + 1

"""
    # Others
        1. two pointer
            def solution(people, limit):
                left, right = 0, len(people) - 1
                people.sort()

                while left < right:
                    if people[left] + people[right] <= limit:
                        left += 1
                    right -= 1

                return len(people) - left
"""