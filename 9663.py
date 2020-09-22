"""
    9663. N-Queen
"""
N = int(input())

answer = 0

rows, down_lefts, down_rights = [0] * N, [0] * (2 * N - 1), [0] * (2 * N - 1)

def do(x):
    global answer 

    if x == N:
        answer += 1
        return
    
    for y in range(N):
        if not (rows[y] or down_lefts[x + y] or down_rights[x - y + N - 1]):
            rows[y] = down_lefts[x + y] = down_rights[x - y + N - 1] = 1
            do(x + 1)
            rows[y] = down_lefts[x + y] = down_rights[x - y + N - 1] = 0

do(x = 0)

print(answer)
