"""
    2730. 색종이 만들기
"""
from sys import stdin

num_of_white, num_of_blue = 0, 0

def cut(left_up, right_down): # 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘름
    global num_of_blue, num_of_white

    if is_blue_colored_paper(left_up, right_down): num_of_blue += 1; return
    elif is_white_colored_paper(left_up, right_down): num_of_white += 1; return

    x1, y1 = left_up
    x2, y2 = right_down

    cut(((x1 + x2) // 2, (y1 + y2) // 2), (x2, y2)) # 4 quadrant
    cut((x1, (y1 + y2) // 2), ((x1 + x2) // 2, y2)) # 3 quadrant
    cut((x1, y1), ((x1 + x2) // 2, (y1 + y2) // 2)) # 2 quadrant
    cut(((x1 + x2) // 2, y1), (x2, (y1 + y2) // 2)) # 1 quadrant

def is_blue_colored_paper(left_up, right_down):
    for y in range(left_up[1], right_down[1]):
        for x in range(left_up[0], right_down[0]):
            if colored_paper[y][x] == 0:
                return False
    return True

def is_white_colored_paper(left_up, right_down):
    for y in range(left_up[1], right_down[1]):
        for x in range(left_up[0], right_down[0]):
            if colored_paper[y][x] == 1:
                return False
    return True

if __name__ == "__main__":
    N = int(stdin.readline().strip()) # N × N(N = 2k, k는 1 이상 7 이하의 자연수)
    colored_paper = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
    
    cut((0, 0), (N, N))
    
    print(num_of_white, num_of_blue, sep = "\n")