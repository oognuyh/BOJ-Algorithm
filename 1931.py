"""
    1931. 회의실 배정
"""
N = int(input()) # 회의의 수 1 ~ 100,000
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings = sorted(meetings, key = lambda meeting : (meeting[1], meeting[0]))

prev_end, count = 0, 0

for meeting in meetings:
    start, end = meeting
    if start >= prev_end:
        prev_end = end 
        count += 1

print(count)
