"""
    167. Two Sum II - Input Array Is Sorted
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            if target < (added := numbers[left] + numbers[right]):
                right -= 1
            elif target > added:
                left += 1
            else:
                return [left + 1, right + 1]
        
"""
    - 65 ms 14.5 MB

    # Others
        1. dictionary - 60 ms 14.7 MB
            pairs = {}

            for i, number in enumerate(numbers):
                if (pair := target - number) in pairs:
                    return [pairs[pair] + 1, i + 1]
                
                pairs[number] = i
"""