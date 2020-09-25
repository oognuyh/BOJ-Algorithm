"""
    9461. 파도반 수열
"""
T = int(input())
cases = [int(input()) for _ in range(T)]
#          1 1 1 2 2 3  4  5  7  9 ..
#          ^ ^ ^ ^ ^ ^  ^  ^  ^  ^
# 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 ..
p = [1, 1, 1, 2, 2] + [0 for _ in range(95)]
for i in range(5, 100): p[i] = p[i - 1] + p[i - 5]

print('\n'.join(map(str, [p[case - 1] for case in cases])))