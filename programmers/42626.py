"""
    42626. 더 맵게
"""
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0

    while scoville:
        least_spicy = heapq.heappop(scoville)
        if least_spicy >= K:
            return mix_count
        
        if not scoville:
            return -1
        
        second_least_spicy = heapq.heappop(scoville)

        heapq.heappush(scoville, least_spicy + (second_least_spicy * 2))
        mix_count += 1