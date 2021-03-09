"""
    1026. 보물
"""
N = int(input())
A = sorted(list(map(int, input().split())), reverse = True)
B = sorted(list(map(int, input().split())))
print(sum(list(map(lambda x: x[0] * x[1], zip(A, B)))))