"""
    1300. k번째 수
"""
from sys import stdin
read = stdin.readline

def run(N, K):
    left, right = 1, K
    
    while left <= right:
        count = 0
        mid = (left + right) // 2

        for i in range(1, N + 1):
            count += min(mid // i, N)

        if count < K:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    
    print(answer)

if __name__ == "__main__":
    run(int(read().strip()), int(read().strip()))