"""
    42584. 주식가격
"""
from typing import List

def solution(prices: List[int]) -> List[int]:
    times = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            times[i] += 1
            if prices[i] > prices[j]: break

    return times