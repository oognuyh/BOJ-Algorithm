"""
    1287. Element Appearing More Than 25% In Sorted Array
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for a, b in zip(arr, arr[len(arr) // 4:]):
            if a == b: return a

"""
    - 115 ms 15.1 MB

    - # Others
        1. Using mode in statistics - 92 ms 15.8 MB
            def findSpecialInteger(self, arr: List[int]) -> int:
                return mode(arr)
        
        2. Counter - 172 ms 15.8 MB
            def findSpecialInteger(self, arr: List[int]) -> int:
                return Counter(arr).most_common(1)[0][0]
"""