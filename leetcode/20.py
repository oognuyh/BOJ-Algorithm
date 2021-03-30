"""
    20. Valid Parentheses
"""
import collections

RIGHT_BRACKETS = [')', '}', ']']
LEFT_BRACKETS = ['(', '{', '[']

class Solution:
    def isValid(self, s: str) -> bool:
        deque = collections.deque()

        for bracket in s:       
            if deque:
                if bracket in LEFT_BRACKETS:
                    deque.append(bracket)
                else:
                    if (deque[-1], bracket) in zip(LEFT_BRACKETS, RIGHT_BRACKETS):
                        deque.pop()
                    else:
                        return False
            else:
                if bracket in RIGHT_BRACKETS:
                    return False
                else:
                    deque.append(bracket)
        
        return False if deque else True

"""
    - 28 ms	14.2 MB

    # Others
        1. dict - 32 ms	14.5 MB
            BRACKETS = {')' : '(', ']' : '[', '}' : '{'}
        
            deque = collections.deque()

            for bracket in s:            
                if deque and bracket in BRACKETS and deque[-1] == BRACKETS[bracket]:
                    deque.pop()
                else:
                    deque.append(bracket)

            return not deque
"""