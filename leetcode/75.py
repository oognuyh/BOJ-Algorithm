"""
    75. Sort Colors
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = 0, 0, len(nums) - 1
        
        while one != two + 1:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1

"""
    - 26 ms	14.1 MB

    # Others
        1. Counter - 36 ms 14.3 MB
            counts = collections.Counter(nums)

            nums[:counts[0]] = [0] * counts[0]
            nums[counts[0]:counts[0] + counts[1]] = [1] * counts[1]
            nums[counts[0] + counts[1]:] = [2] * counts[2]
"""