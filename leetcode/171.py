"""
    171. Number of 1 Bits
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

"""
    - 56 ms	14.2 MB

    # Others
        1. bitwise operator - 56 ms	14.4 MB
            num_of_ones = 0
        
            while n:
                num_of_ones += n & 1
                n >>= 1
                print(bin(n))

            return num_of_ones
"""