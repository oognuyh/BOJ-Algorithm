"""
    232. Implement Queue using Stacks
"""
import collections

class MyQueue:
    def __init__(self):
        self.deque = collections.deque()

    def push(self, x: int) -> None:
        self.deque.append(x)

    def pop(self) -> int:
        return self.deque.popleft() if self.deque else None

    def peek(self) -> int:
        return self.deque[0] if self.deque else None

    def empty(self) -> bool:
        return False if self.deque else True

"""
    - 28 ms	14.5 MB
"""