"""
    704. Binary Search
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[(mid := left + (right - left) // 2)] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1

"""
    - 244 ms 15.6 MB

    # Others
        1. bisect - 240 ms 15.6 MB
            return index if (index := bisect.bisect_left(nums, target)) < len(nums) and nums[index] == target else -1
"""