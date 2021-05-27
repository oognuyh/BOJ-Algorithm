"""
    46. Permutations
"""
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)

"""
    - 36 ms	14.3 MB	

    # Others
        1. dfs - 32 ms 14.5 MB
            res = []
            lev, avail, lev_node = 0, nums, []
            N = len(nums)
            def dfs(lev, avail, lev_node):
                if lev == N:
                    res.append(lev_node)
                    return
                for i in range(len(avail)):
                    dfs(lev + 1, avail[:i] + avail[i+1:], lev_node + [avail[i]])
            
            dfs(lev, avail, lev_node)
            
            return(res)
"""