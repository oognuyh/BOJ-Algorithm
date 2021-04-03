"""
    622. Design Circular Queue
"""
import collections

class MyCircularQueue:
    def __init__(self, k: int):
        self.deque = collections.deque(maxlen = k)

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.deque.append(value)        

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.deque.popleft()

        return True

    def Front(self) -> int:
        return self.deque[0] if self.deque else -1

    def Rear(self) -> int:
        return self.deque[-1] if self.deque else -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.deque.maxlen

"""
    - 72 ms	15 MB	

    # Tips
        1. deque.maxlen takes more time than defined maxlen(72 ms > 64 ms)
"""