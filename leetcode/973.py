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
        1. heapq - 852 ms 19.8 MB
            hq = list(map(lambda point: (get_distance(*point), point), points))
         
            heapq.heapify(hq)
        
            return [point for d, point in heapq.nsmallest(k, hq)]
"""