"""
    2110. 공유기 설치
"""
from sys import stdin

def run(N, C):
    def get_coord():
        return sorted([int(stdin.readline().strip()) for _ in range(N)])

    def count():
        count = 1
        v = coord[0]

        for i in range(1, len(coord)):
            if coord[i] >= mid + v:
                count += 1
                v = coord[i]

        return count
    
    coord = get_coord()

    start = 1
    end = coord[-1]

    answer = 0

    while start <= end:
        mid = (start + end) // 2
        
        if count() >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)

if __name__ == "__main__":
    run(*map(int, stdin.readline().strip().split()))