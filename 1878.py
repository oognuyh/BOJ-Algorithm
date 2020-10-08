"""
    1878. 스택 수열
"""
N = int(input())
targets = [int(input()) for _ in range(N)]
number, stack, answer = 1, [], []

def push(number):
    global stack, answer
    
    answer += ['+']
    stack += [number]

def pop():
    global stack, targets, answer

    answer += ['-']
    stack.pop()
    targets.pop(0)

while targets:  
    if number <= targets[0]: # push
        push(number)
        if number == targets[0]: # pop
            pop()
        number += 1
    else: # pop
        if stack:
            if stack[-1] == targets[0]: # pop
                pop()
            else:
                break
        else: # impossible
            break

print('\n'.join(answer) if not targets else 'NO')