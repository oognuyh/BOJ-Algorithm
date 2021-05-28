"""
    77. Combinations
"""
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))

"""
    - 80 ms 15.5 MB

    # Others
        1. dfs - 460 ms	15.7 MB
             results = []
        
            def dfs(elements, start: int, k : int):
                if k == 0:
                    results.append(elements[:])
                
                for i in range(start, n + 1):
                    elements.append(i)
                    dfs(elements, i + 1, k - 1)
                    elements.pop()

            dfs([], 1, k)

            return results
"""