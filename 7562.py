"""
    7562. 나이트의 이동
"""
from collections import deque
from sys import stdin
read = lambda : stdin.readline().strip()

def run(T):
    def get_case():
        board_length = int(read())
        start_x, start_y = map(int, read().split())
        end_x, end_y = map(int, read().split())
        return board_length, start_x, start_y, end_x, end_y

    def is_end():
        return (x, y) == (end_x, end_y)

    def is_in_range():
        return -1 < next_x and next_x < board_length and -1 < next_y and next_y < board_length

    dx = (2, 1, -1, -2, -2, -1, 1, 2)
    dy = (1, 2, 2, 1, -1, -2, -2, -1)

    for _ in range(T):
        board_length, start_x, start_y, end_x, end_y = get_case()
        board = [[0 for _ in range(board_length)] for _ in range(board_length)]

        queue = deque([(start_x, start_y)])

        while queue:
            x, y = queue.popleft()
            if is_end():
                print(board[x][y]); break

            for _dx, _dy in zip(dx, dy):
                next_x, next_y = x + _dx, y + _dy
                if is_in_range():
                    if not board[next_x][next_y]:
                        board[next_x][next_y] = board[x][y] + 1
                        queue.append((next_x, next_y))

if __name__ == "__main__":
    run(int(read()))