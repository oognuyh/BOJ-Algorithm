"""
    11053. 가장 긴 증가하는 부분 수열
"""
N, A = int(input()), list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1, len(A)):
    try:
        dp[i] = max([dp[j] for j in range(i) if A[i] > A[j]]) + 1
    except:
        pass
    
print(max(dp))