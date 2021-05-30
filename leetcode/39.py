"""
    39. Combination Sum
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(remain: int, index: int, path: List[int]):
            if remain == 0:
                results.append(path)
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] > remain: break
                
                dfs(remain - candidates[i], i, path + [candidates[i]])
                
        results = []
        candidates.sort()
        
        dfs(target, 0, [])
        
        return results

"""
    - 44 ms	14.3 MB

    # Others
        1. DP - 52 ms 14.8 MB
            dp = [[] for _ in range(target + 1)]
            
            for candidate in candidates:                                  
                for i in range(candidate, target + 1):                      
                    if i == candidate: 
                        dp[i].append([candidate])
                    for comb in dp[i - candidate]: 
                        dp[i].append(comb + [candidate]) 
                        
            return dp[-1]
"""