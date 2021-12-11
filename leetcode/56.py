"""
    56. Merge Intervals
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = list()
        
        for interval in sorted(intervals, key = lambda interval: interval[1]):
            if merged and interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged

"""
    - 80 ms 16.1 MB

    # Tips
        1. merged += interval, is similar to merged.append(interval)
           but the latter is faster since the former is allocating a new list in memory
"""