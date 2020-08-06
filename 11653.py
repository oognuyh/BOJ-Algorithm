"""
    11653. 소인수분해
"""
N = int(input())

target = 2

while N > 1:
    if N % target != 0:
        while N % target != 0: target += 1
    N /= target 
    print(target)