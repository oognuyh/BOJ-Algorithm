"""
    1260. DFS와 BFS
"""
from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

def run(N, M, V):
    def dfs(v):
        print(v, end = " ")

        dfs_visited[v] = True

        for to in range(1, N + 1):
            if not dfs_visited[to] and graph[v][to]:
                dfs(to)

    def bfs(v):
        print()

        bfs_visited[v] = True
        q = deque([v])

        while q:
            _v = q.popleft()
            
            print(_v, end = " ")
            
            for to in range(1, N + 1):
                if not bfs_visited[to] and graph[_v][to]:
                    q.append(to)
                    bfs_visited[to] = True
    
    graph = [[False for x in range(N + 1)] for y in range(N + 1)]
    
    for _ in range(M):
        _from, _to = map(int, read().split())
        graph[_from][_to], graph[_to][_from] = True, True

    dfs_visited = [False for _ in range(N + 1)]
    bfs_visited = [False for _ in range(N + 1)]

    dfs(V)
    bfs(V)

if __name__ == "__main__":
    run(*map(int, read().split()))
