"""
    771. Jewels and Stones
"""
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_counter = collections.Counter(stones)
        jewels = list(map(str, jewels))
        
        return sum(v for k, v in stones_counter.items() if k in jewels)
"""
    - 28 ms 14.3 MB

    # Others 
        1. map - 28 ms 14.2 MB
            return sum(map(stones.count, list(jewels)))

        2. counter + for - 28 ms 14.3 MB
            counter = collections.Counter(stones)

            return sum(Counter[j] for j in jewels)
"""