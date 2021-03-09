"""
    11650. 좌표 정렬하기
"""
N = int(input())
points = sorted([list(map(int, input().split())) for _ in range(N)])

for point in points: print(point[0], point[1])