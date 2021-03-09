"""
    1992. 쿼드트리
"""
from sys import stdin

WHITE, BLACK = '0', '1' #  흰 점을 나타내는 0과 검은 점을 나타내는 1

def divide(left_up, right_down) -> str: # 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나눔
    if is_all_white(left_up, right_down):
        return WHITE
    elif is_all_black(left_up, right_down):
        return BLACK

    x1, y1 = left_up
    x2, y2 = right_down
    
    answer = "("

    answer += divide((x1, y1), ((x1 + x2) // 2, (y1 + y2) // 2)) # 2 quadrant
    answer += divide(((x1 + x2) // 2, y1), (x2, (y1 + y2) // 2)) # 1 quadrant
    answer += divide((x1, (y1 + y2) // 2), ((x1 + x2) // 2, y2)) # 3 quadrant
    answer += divide(((x1 + x2) // 2, (y1 + y2) // 2), (x2, y2)) # 4 quadrant

    answer += ")"

    return answer

def is_all_white(left_up, right_down) -> bool:
    for y in range(left_up[1], right_down[1]):
        for x in range(left_up[0], right_down[0]):
            if pixels[y][x] == BLACK:
                return False
    return True

def is_all_black(left_up, right_down) -> bool:
    for y in range(left_up[1], right_down[1]):
        for x in range(left_up[0], right_down[0]):
            if pixels[y][x] == WHITE:
                return False
    return True

if __name__ == "__main__":
    N = int(stdin.readline().strip()) # N 은 언제나 2의 제곱수로 주어지며, 1≤N ≤64
    pixels = [list(map(str, stdin.readline().strip())) for _ in range(N)]
    
    print(divide((0, 0), (N, N)))
