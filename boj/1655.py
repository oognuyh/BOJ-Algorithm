"""
    1655. 가운데를 말해요
"""
from sys import stdin 
import heapq 

max_heap, min_heap = [], []

def run(x):
    def push():
        heapq.heappush(max_heap, (-x, x)) if len(max_heap) == len(min_heap) else heapq.heappush(min_heap, x)
    
    def swap_each_root():
        if min_heap:
            min_heap_root = min_heap[0]
            max_heap_root = max_heap[0][1]
            if max_heap_root > min_heap_root:
                heapq.heapreplace(max_heap, (-min_heap_root, min_heap_root))
                heapq.heapreplace(min_heap, max_heap_root)

    push()
    swap_each_root()

    print(max_heap[0][1])

if __name__ == "__main__":
    N = int(stdin.readline().strip())

    for _ in range(N):
        run(int(stdin.readline().strip()))