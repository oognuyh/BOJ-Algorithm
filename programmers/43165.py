"""
    43165. 타켓 넘버
"""
def solution(numbers, target):    
    def calculate(index, value):
        nonlocal count
        
        if index == len(numbers):
            count = count + 1 if value == target else count
            return
    
        calculate(index + 1, value + numbers[index])
        calculate(index + 1, value - numbers[index])
    
    count = 0
    
    calculate(0, 0)
    
    return count

"""
    # Others
        1. simplify
            def solution(numbers, target):
                if not numbers:
                    return 1 if target == 0 else 0
                else:
                    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

        2. map with itertools.product
            def solution(numbers, target):
                l = [(x, -x) for x in numbers]
                s = map(sum, product(*l))

                return s.count(target)
"""