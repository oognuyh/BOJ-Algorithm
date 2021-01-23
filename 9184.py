"""
    9184. 신나는 함수 실행
"""
from sys import stdin

MAX = 20

def run():
    def create_w():
        w = [[[1 for _ in range(MAX + 1)] for _ in range(MAX + 1)] for _ in range(MAX + 1)]
        
        for a in range(1, MAX + 1):
            for b in range(1, MAX + 1):
                for c in range(1, MAX + 1):
                    w[a][b][c] = w[a][b][c - 1] + w[a][b - 1][c - 1] - w[a][b - 1][c] if a < b and b < c else w[a - 1][b][c] + w[a - 1][b - 1][c] + w[a - 1][b][c - 1] - w[a - 1][b - 1][c - 1]

        return w

    def is_end():
        return True if [a, b, c] == [-1, -1, -1] else False
    
    w = create_w()

    while True:
        a, b, c = map(int, stdin.readline().strip().split())
        if is_end(): break
        
        print(f"w({a}, {b}, {c}) = ", end = "")
        print(1 if a < 1 or b < 1 or c < 1 else w[20][20][20] if a > 20 or b > 20 or c > 20 else w[a][b][c])
        
if __name__ == "__main__":
    run()