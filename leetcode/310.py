"""
    310. Minimum Height Trees
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        prev_leaves = leaves = [x for x in range(n) if len(graph[x]) <= 1]
         
        while leaves:
            new_leaves = []

            for leaf in leaves:
                if not graph[leaf]: return leaves

                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            prev_leaves, leaves = leaves, new_leaves
                
        return prev_leaves

"""
    - 240 ms 19.1 MB
"""