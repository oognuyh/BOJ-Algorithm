"""
    78. Subsets
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets

"""
    - 24 ms	14.6 MB

    # Others
        1. reduce - 32 ms 14.7 MB
            return reduce(lambda subsets, n: subsets + [s+[n] for s in subsets], nums, [[]])        

        2. combinations - 32 ms 14.4 MB
            return [s for n in range(len(nums)+1)
                    for s in itertools.combinations(nums, n)]
        3. integers as bit mask - 36 ms 14.6 MB
            return [[nums[i] for i in range(len(nums)) if mask >> i & 1]
                    for mask in range(2 ** len(nums))]
"""