"""
    239. Sliding Window Maximum
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq, maximums = collections.deque(), []
        
        for i, num in enumerate(nums):
            print(dq, maximums)
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            
            maximums.append(nums[dq[0]])
        
        return maximums[k - 1:]

"""
    - 1800 ms 30.3 MB
"""