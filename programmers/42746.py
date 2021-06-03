"""
    42746. 가장 큰 수(정렬)
"""
from functools import cmp_to_key

def solution(numbers):
    return str(int(''.join(sorted(map(str, numbers), key = cmp_to_key(lambda x, y: -1 if int(x + y) > int(y + x) else 1)))))

"""
    # Others
        1. lambda s: s * 3
            def solution(numbers):
                numbers = list(map(str, numbers))
                numbers.sort(key = lambda x: x * 3, reverse = True)
                return str(int(''.join(numbers)))
"""