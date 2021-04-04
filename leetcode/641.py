"""
    641. Design Circular Deque
"""
import collections 

class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = collections.deque()
        self.max_len = k

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False

        self.deque.appendleft(value)

        return True        

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False

        self.deque.append(value)

        return True        

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False

        self.deque.popleft()

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False

        self.deque.pop()

        return True        

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty(): return -1

        return self.deque[-1]        

    def isEmpty(self) -> bool:
        return False if self.deque else True
        
    def isFull(self) -> bool:
        return True if len(self.deque) == self.max_len else False

"""
    - 68 ms	15 MB
"""