"""
    238. Product of Array Except Self
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
    
        mx = 1               
        for i in range(len(nums)):
            ans[i] = mx     
            mx *= nums[i]   
        
        mx = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= mx  
            mx *= nums[j]

        return ans 

"""
    - 240 ms 20.9 MB
"""