"""
    424. Longest Repeating Character Replacement
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts, left = collections.Counter(), 0
        
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            
            max_count = counts.most_common(1)[0][1]
            
            if right - left - max_count > k:
                counts[s[left]] -= 1
                left += 1
                
        return right - left

"""
    - 464 ms 14.4 MB
"""