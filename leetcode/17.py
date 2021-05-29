"""
    17. Letter Combinations of a Phone Number
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def dfs(index, path):
            if len(path) == len(digits):
                results.append(path)
                return
            
            for i in dic[digits[index]]:
                dfs(index + 1, path + i)
        
        results = []
        
        dfs(0, "")
        
        return results

"""
    - 28 ms 14.5 MB
"""