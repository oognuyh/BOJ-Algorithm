"""
    76. Minimum Window Substring
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = collections.Counter(t), len(t)
        left = start = end = 0
        
        for right, character in enumerate(s, 1):
            missing -= need[character] > 0
            need[character] -= 1
            
            if not missing:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1                    
                
                if not end or right - left <= end - start:
                    start, end = left, right
        
        return s[start:end]

"""
    - 120 ms 15 MB
"""