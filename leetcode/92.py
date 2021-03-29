"""
    92. Reverse Linked List II
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
    
        cur_dummy = dummy = ListNode(0, head)
        for  _ in range(left - 1):
            cur_dummy = cur_dummy.next

        l = r = cur_dummy.next
        for _ in range(right - left):
            l, r.next.next, r.next = r.next, l, r.next.next
        
        cur_dummy.next = l

        return dummy.next

"""
    - 28 ms	14.2 MB
"""