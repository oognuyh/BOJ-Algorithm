"""
    1012. 유기농 배추
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
read = lambda : stdin.readline().strip()

def run(T):
    def move(x, y):
        field[y][x] = False

        nexts = [(x + _dx, y +_dy) for _dx, _dy in zip(dx, dy) if -1 < x + _dx and x + _dx < width and -1 < y + _dy and y + _dy < height and field[y + _dy][x + _dx]]

        for next in nexts:
            move(*next)

    dx = (-1, 0, 0, 1)
    dy = (0, -1, 1, 0)
    
    for _ in range(T):
        width, height, num_of_cabbages = map(int, read().split()) 
        cabbage_locations = [tuple(map(int, read().split())) for _ in range(num_of_cabbages)] 
        count = 0

        field = [[True if (x, y) in cabbage_locations else False for x in range(width)] for y in range(height)]

        for y in range(height):
            for x in range(width):
                if field[y][x]:
                    move(x, y)
                    count += 1

        print(count)

if __name__ == "__main__":
    run(int(read()))    
