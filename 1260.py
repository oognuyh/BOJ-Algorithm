"""
    1260. DFS와 BFS
"""
from sys import stdin
read = lambda : stdin.readline().strip()

def run(N, M, V):
    def dfs(v):
        print(v, end=' ')
        visited[v] = True
        for to in range(1, N + 1):
            if not visited[to] and graph[v][to]:
                dfs(to)

    def bfs(v):
        q = [v]
        visited[v] = False

        while q:
            v = q[0]
            print(v, end=' ')
            del q[0]
            for i in range(1, N + 1):
                if visited[i] == 1 and graph[v][i] == 1:
                    q.append(i)
                    visited[i] = 0
    
    connections = [tuple(map(int, read().split())) for _ in range(M)]
    graph = [[True if (x, y) in connections or (y, x) in connections else False for x in range(N + 1)] for y in range(N + 1)]

    visited = [False for _ in range(N + 1)]

    dfs(v)
    print()
    bfs(v)


if __name__ == "__main__":
    run(*map(int, read().split()))