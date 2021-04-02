"""
    225. Implement Stack using Queues
"""
import collections

class MyStack:
    def __init__(self):
        self.stack = collections.deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        
    def empty(self) -> bool:
        return False if self.stack else True

"""
    - 32 ms 14.2 MB 
"""