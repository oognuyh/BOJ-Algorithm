"""
    561. Array Partition I
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

"""
    - 244 ms 16.7 MB
"""