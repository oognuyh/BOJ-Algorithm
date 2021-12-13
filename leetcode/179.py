"""
    179. Largest Number
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def should_swap(one: int, another: int) -> bool:
            return one + another < another + one
        
        for i in range(1, len(nums := list(map(str, nums)))):
            j = i
            
            while j > 0 and should_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
        
        return str(int(''.join(nums)))
            
"""
    - 52 ms 14.1 MB

    # Others
        1. inherit - 32 ms 14.3 MB
            class Number(str):
                def __lt__(x, y) -> bool:
                    return x + y > y + x
            
            class Solution:
                def largestNumber(self, nums: List[int]) -> str:
                    return str(int(''.join(sorted(map(Number, nums)))))
"""