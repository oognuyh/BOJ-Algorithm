"""
    15596. 정수 N개의 합
"""
def solve(numbers):
    return sum(numbers)

print(solve(list(map(int, input().split()))))