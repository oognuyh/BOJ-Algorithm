"""
    242. Valid Anagram
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        return collections.Counter(s) == collections.Counter(t)

"""
    - 52 ms 14.6 MB
"""    