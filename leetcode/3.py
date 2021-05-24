"""
    3. Longest Substring Without Repeating Characters
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        substring, max_length = s[0], 1
        
        for letter in s[1:]:
            if letter in substring:
                index = substring.find(letter)
                substring = substring[index + 1:]
            
            substring += letter
            
            if len(substring) > max_length:
                max_length = len(substring)
                
        return max_length

"""
    - 44 ms	14.3 MB

    # Others
        1. Sliding Window + Two Pointers - 44 ms 14.3 MB
            used = {}
            max_length = start = 0
            
            for index, letter in enumerate(s):
                if letter in used and start <= used[letter]:
                    start = used[letter] + 1
                else:
                    max_length = max(max_length, index - start + 1)
                    
                used[letter] = index
                
            return max_length
"""