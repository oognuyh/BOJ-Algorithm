"""
    973. K Closet Points to Origin
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point: List[int]) -> int:
            x, y = point

            return x ** 2 + y ** 2
        
        return sorted(points, key = get_distance)[:k]

"""
    - 624 ms 19.7 MB

    # Others
        1. heapq - 656 ms 19.8 MB
            return heapq.nsmallest(k, points, get_distance)
"""