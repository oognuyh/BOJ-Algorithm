"""
    5430. AC
"""
from sys import stdin
from collections import deque

T = int(stdin.readline().strip()) # number of test cases

for _ in range(T): # each test case
    ps = stdin.readline().strip()
    n = int(stdin.readline().strip())
    try:
        array = deque(map(int, stdin.readline().strip().rstrip(']').lstrip('[').split(',')))
    except:
        array = deque() # if get an empty array

    is_error = False
    reverse_count = 0

    for p in ps:
        if p == 'R': # reversed function must be called once
            reverse_count += 1
        else:   
            if array:
                array.popleft() if reverse_count % 2 == 0 else array.pop()
            else:
                is_error = True
                break
    # no spaces btw commas
    print('error' if is_error else '[' + ','.join(map(str, array if reverse_count % 2 == 0 else reversed(array))) + ']')