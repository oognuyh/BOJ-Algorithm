"""
    2981. 검문
"""
def gcd(a, b):
    while b:
        a, b = b, a % b 
    return a 
    
N = int(input()) 
numbers = [int(input()) for _ in range(N)]

numbers.sort(reverse = True)

numbers = [numbers[i] - numbers[i + 1] for i in range(len(numbers) - 1)]

element = numbers[0]
for i in range(1, len(numbers)): element = gcd(element, numbers[i])

answer = [element] if element > 1 else []

for i in range(2, int(element ** (1/2)) + 1):
    if element % i == 0: 
        answer.append(i)
        if not element // i == i: answer.append(element // i)

print(' '.join(map(str, sorted(answer))))