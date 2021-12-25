"""
    136. Single Number
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

"""
    - 124 ms 16.6 MB

    # Others
        1. xor - 200 ms	16.7 MB
            return reduce(lambda x, y: x ^ y, nums)
"""