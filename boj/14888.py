"""
    14888. 연산자 끼워넣기
"""
from copy import deepcopy

minimum = 987654321
maximum = -987654321

def convert(operators):
    temp = []
    for i in range(len(operators)):
        if operators[i] > 0:
            for _ in range(operators[i]):
                temp.append('+' if i == 0 else '-' if i == 1 else '*' if i == 2 else '/')

    return temp 

def do(numbers, operators, value):
    global minimum, maximum

    # exit
    if not numbers:
        print(value)
        if minimum > value: minimum = value
        if maximum < value: maximum = value
        return
    
    number = numbers.pop(0)
    print(value)

    # do
    if '+' in operators:
        temp = deepcopy(operators)
        temp.remove('+')
        do(deepcopy(numbers), temp, value + number)
    if '-' in operators:
        temp = deepcopy(operators)
        temp.remove('-')
        do(deepcopy(numbers), temp, value - number)
    if '*' in operators:
        temp = deepcopy(operators)
        temp.remove('*')
        do(deepcopy(numbers), temp, value * number)
    if '/' in operators:
        temp = deepcopy(operators)
        temp.remove('/')
        do(deepcopy(numbers), temp, value // number if value > 0 else -(-value // number))


if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    operators = convert(operators)      

    number = numbers.pop(0)
    do(numbers, operators, number)

    print(maximum, minimum, sep = '\n')