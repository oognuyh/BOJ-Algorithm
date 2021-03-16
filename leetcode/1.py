"""
    1. Two Sum
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        for i in range(length):
            for j in range(length):
                if i == j: continue
        
                if nums[i] + nums[j] == target:
                   return [i, j]

"""
    - 44 ms 14.5 MB

    # Others 
        1. dict - 36 ms 14.3 MB
            dic = {}
            for i, num in enumerate(nums):
                if num in dic:
                    return [dic[num], i]
                else:
                    dic[target - num] = i
"""