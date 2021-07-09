"""
    743. Network Delay Time
"""
import collections, heapq 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        q = [(0, k)]
        dist = collections.defaultdict(int)
        
        while q:
            time, node = heapq.heappop(q)
            
            if node not in dist:
                dist[node] = time
                
                for v, w in graph[node]:
                    heapq.heappush(q, (time + w, v))
                    
        return max(dist.values()) if len(dist) == n else -1
    
"""
    - 484 ms 16.2 MB
    
    # Others
        1. set - 584 ms 16.3 MB
            def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
                graph = collections.defaultdict(list)
                
                for u, v, w in times:
                    graph[u].append((v, w))
                    
                q = [(0, k)]
                visited = set()
                answer = 0
                
                while q:
                    time, node = heapq.heappop(q)
                    
                    if node not in visited:
                        visited.add(node)
                        answer = max(answer, time)
                        
                        for v, w in graph[node]:
                            if v not in visited:
                                heapq.heappush(q, (time + w, v))
                            
                return answer if len(visited) == n else -1
"""