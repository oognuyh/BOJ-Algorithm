"""
    344. Reverse String
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
    
"""
    - 180 ms 18.7 MB

    # Others 
        1. reverse - 184 ms 18.7 MB
            s.reverse()

        2. two pointer - 196 ms 18.6 MB
            left, right = 0, len(s) - 1
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

    # Tips
        1. s[:] = s[::-1] doesn't allocate extra space
"""