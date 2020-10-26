"""
    1780. 종이의 개수
"""
from sys import stdin

count = [0, 0, 0] # -1, 0, 1

def cut(left_up, right_down):
    if is_full(left_up, right_down):
        return
    
    x1, y1 = left_up
    x2, y2 = right_down

    cut((x1, y1), (x1 + (x2 - x1) // 3, y1 + (y2 - y1) // 3)) # left up
    cut((x1, y1 + (y2 - y1) // 3), (x1 + (x2 - x1) // 3, y1 + (y2 - y1) // 3 * 2)) # left
    cut((x1, y1 + (y2 - y1) // 3 * 2), (x1 + (x2 - x1) // 3, y2)) # left down
    
    cut((x1 + (x2 - x1) // 3, y1), (x1 + (x2 - x1) // 3 * 2, y1 + (y2 - y1) // 3)) # up
    cut((x1 + (x2 - x1) // 3, y1 + (y2 - y1) // 3), (x1 + (x2 - x1) // 3 * 2, y1 + (y2 - y1) // 3 * 2)) # center
    cut((x1 + (x2 - x1) // 3, y1 + (y2 - y1) // 3 * 2), (x1 + (x2 - x1) // 3 * 2, y2)) # down
    
    cut((x1 + (x2 - x1) // 3 * 2, y1), (x2, y1 + (y2 - y1) // 3)) # right up
    cut((x1 + (x2 - x1) // 3 * 2, y1 + (y2 - y1) // 3), (x2, y1 + (y2 - y1) // 3 * 2)) # right
    cut((x1 + (x2 - x1) // 3 * 2, y1 + (y2 - y1) // 3 * 2), (x2, y2)) # right down

def is_full(left_up, right_down) -> bool:
    global count

    value = ''.join([paper[y][x] for y in range(left_up[1], right_down[1]) for x in range(left_up[0], right_down[0])])
    num_of_cells = (right_down[0] - left_up[0]) * (right_down[1] - left_up[1])

    if "1" * num_of_cells == value: # 1
        count[2] += 1
    elif "0" * num_of_cells == value: # 0
        count[1] += 1
    elif "-1" * num_of_cells == value: # -1
        count[0] += 1
    else: # not full
        return False
    
    return True

if __name__ == "__main__": 
    N = int(stdin.readline().strip()) # N x N의 행렬로 표현되는 종이
    paper = [list(map(str, stdin.readline().strip().split())) for _ in range(N)]

    cut((0, 0), (N, N))

    print('\n'.join(map(str, count)))
