"""
    2178. 미로 탐색
"""
from collections import deque

def do():
    def is_in_range(x, y):
        return True if -1 < x and x < M and -1 < y and y < N and board[y][x] else False
    
    def get_valid_directions(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # LEFT, RIGHT, UP, DOWN
        return [(x + to_x, y + to_y) for to_x, to_y in directions if is_in_range(x + to_x, y + to_y)]
    
    dist = [[1 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0)]); board[0][0] = 0

    while queue:
        x, y = queue.popleft()
        for _x, _y in get_valid_directions(x, y):
            board[_y][_x] = 0
            dist[_y][_x] = dist[y][x] + 1
            queue.append((_x, _y))
    
    return dist[N - 1][M - 1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]
   
    print(do())