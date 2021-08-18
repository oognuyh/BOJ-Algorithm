"""
    215. Kth Largest Element in an Array
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True)[k - 1]

"""
    - 56 ms 14.9 MB

    # Others
        1. heapq.nlargest - 64 ms 15.2 MB
            return heapq.nlargest(k, nums)[-1]
"""