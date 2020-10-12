"""
    2751. 수 정렬하기 2
"""
N = int(input()) # 수의 개수 1 ~ 1,000,000
numbers = [int(input()) for _ in range(N)]

for number in sorted(numbers): print(number)