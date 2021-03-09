"""
    125. Valid Palindrome
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [character for character in s.lower() if character.isalnum()] 
            
        return s == s[::-1]

"""
    - 36 ms 15.9 MB

    # Others 
        1. filter - 36 ms 15.2 MB
            s = ''.join(filter(str.isalnum(), s.lower())

        2. re - 36 ms 15.8 MB
            s = re.sub('[^a-z0-9]', '', s)

    # Tips
        1. [::-1] is faster than reverse()
"""