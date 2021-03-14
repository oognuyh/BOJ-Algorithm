"""
    49. Group Anagrams
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        group = defaultdict(list)        
        
        for s in strs:
            group[''.join(sorted(s))].append(s)
        
        return list(group.values())

"""
    - 88 ms 17.2 MB

    # Tips
        1. dict.values() returns list
"""