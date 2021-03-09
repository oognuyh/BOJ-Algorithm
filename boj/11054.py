"""
    11054. 가장 긴 바이토닉 부분 수열
"""
N = int(input())

A = list(map(int, input().split())); reversed_A = A[::-1]
dp, reversed_dp = [1 for _ in range(N)], [1 for _ in range(N)]

for i in range(1, N):
    try: dp[i] = max([dp[j] for j in range(i) if A[i] > A[j]]) + 1
    except: pass
    try: reversed_dp[i] = max([reversed_dp[j] for j in range(i) if reversed_A[i] > reversed_A[j]]) + 1
    except: pass

print(max(map(lambda xy: xy[0] + xy[1], zip(dp, reversed(reversed_dp)))) - 1)