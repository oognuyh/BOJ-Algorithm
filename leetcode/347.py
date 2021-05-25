"""
    347. Top K Frequent Elements
"""
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda pair: pair[0], collections.Counter(nums).most_common(k)))

"""
    - 84 ms	18.7 MB	

    # Others
        1. Min Heap - 100 ms 18.6 MB
            d = defaultdict(int)

            for i in nums:
                d[i] = d[i] + 1
            heap = []
            for key, val in d.items():
                if len(heap) < k:
                    heapq.heappush(heap,(val,key))
                else:
                    if val > heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap,(val,key))
            
            tmp = []
            for i in heap:
                tmp.append(i[1])
            
            return tmp
"""