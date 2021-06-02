"""
    207. Course Schedule
"""
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced, visited = set(), set()
        
        def dfs(i: int) -> bool:
            if i in traced: return False
            if i in visited: return True
            
            traced.add(i)
            
            for y in graph[i]:
                if not dfs(y): return False
                
            traced.remove(i)
            visited.add(i)
            
            return True
        
        for x in list(graph):
            if not dfs(x): return False
            
        return True

"""
    - 92 ms	17.8 MB

    # Others
        1. list, bfs - 92 ms 15.6 MB
            n = numCourses
            graph = [[] for _ in range(n)]
            g = [0] * n

            for v, u in prerequisites:
                graph[u].append(v)
                g[v] += 1
            
            S = [ v for v in range(n) if g[v] == 0]
            
            while S:
                u = S.pop()
                for v in graph[u]:
                    g[v] -= 1
                    if g[v] == 0:
                        S.append(v)

            return not any(g)
"""