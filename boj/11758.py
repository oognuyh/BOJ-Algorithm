"""
    11758. CCW
"""
from sys import stdin 

def get():
    S = (P[1][0] - P[0][0]) * (P[2][1] - P[0][1]) - (P[1][1] - P[0][1]) * (P[2][0] - P[0][0])

    if S > 0: # 반시계
        return 1
    elif S == 0: # 일직선
        return 0
    else: # 시계
        return -1

if __name__ == "__main__":
    P = [list(map(int, stdin.readline().strip().split())) for _ in range(3)]

    print(get())