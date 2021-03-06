"""
    1012. 유기농 배추

    [TODO]
    - 상하좌우 영역 찾기
    - 한 영역 찾고 1인 지역 다시 탐색
    - count += 1
"""
from sys import stdin
from collections import deque
read = lambda : stdin.readline().strip()

def run(T):
    def move(target):
        x, y = target
        field[y][x] = False

        next_targets = [(x + _dx, y +_dy) for _dx, _dy in zip(dx, dy) if -1 < x + _dx and x + _dx < width and -1 < y + _dy and y + _dy < height and field[y + _dy][x + _dx]]

        for next_target in next_targets:
            x, y = next_target
            field[y][x] = False
            move(next_target)

    dx = (-1, 0, 0, 1)
    dy = (0, -1, 1, 0)
    
    for _ in range(T):
        width, height, num_of_cabbages = map(int, read().split()) # width, height, num of cabbages
        cabbage_locations = [tuple(map(int, read().split())) for _ in range(num_of_cabbages)] # (x, y)
        count = 0

        field = [[True if (x, y) in cabbage_locations else False for x in range(width)] for y in range(height)]

        for y in range(height):
            for x in range(width):
                if field[y][x]:
                    field[y][x] = False
                    move((y, x))
                    count += 1

        print(f"\nnum of worms = {count}")

if __name__ == "__main__":
    run(int(read()))