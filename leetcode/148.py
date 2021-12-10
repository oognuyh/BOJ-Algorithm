"""
    148. Sort List
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)

        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next
    
        tail.next = h1 or h2

        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
    
        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

"""
    - 488 ms 30.3 MB
"""