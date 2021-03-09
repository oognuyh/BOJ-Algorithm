"""
    10972. 다음 순열
"""
N = int(input())
permutation = list(map(int, input().split()))
try:
    i = max([index for index in range(len(permutation) - 1) if permutation[index] < permutation[index + 1]])
    j = max([index for index in range(i + 1, len(permutation)) if permutation[i] < permutation[index]])

    permutation[i], permutation[j] = permutation[j], permutation[i]

    permutation = permutation[:i + 1] + sorted(permutation[i + 1:])

    print(" ".join(map(str, permutation)))
except: # already set
    print("-1")