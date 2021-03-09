"""
    11651. 좌표 정렬하기 2
"""
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points = sorted(points, key = lambda x: (x[1], x[0]))
for point in points: print(point[0], point[1])