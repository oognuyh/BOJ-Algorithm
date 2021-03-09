'''
    15649. N과 M (1)
'''
import itertools 
N, M = map(int, input().split())
target = map(str, range(1, N +1))
for answer in list(map(' '.join, itertools.permutations(target, M))): print(answer)