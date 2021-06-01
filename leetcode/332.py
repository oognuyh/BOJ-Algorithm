"""
    332. Reconstruct Itinerary
"""
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for starting, destination in sorted(tickets):
            graph[starting].append(destination)
            
        route = []
        
        def dfs(starting):
            while graph[starting]:
                dfs(graph[starting].pop(0))
                
            route.append(starting)
            
        dfs('JFK')
        
        return route[::-1]

"""
    - 164 ms 14.9 MB

    # Others
        1. stack - 120 ms 14.4 MB
            graph = collections.defaultdict(list)
            
            for starting, destination in sorted(tickets):
                graph[starting].append(destination)
                
            route, stack = [], ['JFK']
            
            while stack:
                while graph[stack[-1]]:
                    stack.append(graph[stack[-1]].pop(0))
                    
                route.append(stack.pop())
                
            return route[::-1]

        2. graph[key].sort() - 68 ms 14.7 MB
            graph = defaultdict(list)
            
            for src, dest in tickets:
                graph[src].append(dest)
            
            for key in graph:
                graph[key].sort(reverse = True)
                
            ans = []
            
            def dfs(node):
                
                while graph[node]:
                    dfs(graph[node].pop())
                
                ans.append(node)
            
            dfs("JFK")

            return ans[::-1]
"""