"""
    12977. 소수 만들기
"""
from typing import List, Tuple
from itertools import combinations

def solution(nums: List[int]) -> int:
    def is_prime(num: int) -> bool:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    return len(set([num for num in combinations(nums, 3) if is_prime(sum(num))]))