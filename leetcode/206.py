"""
    206. Reverse Linked List
"""
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head

        deque = collections.deque()
        
        while head:
            deque.append(head.val)
            head = head.next
        
        reversed_nodes = ListNode()
        cur = reversed_nodes

        while deque:
            element = deque.pop()
            cur.val = element
            cur.next = ListNode() if deque else None
            cur = cur.next

"""
    - 44 ms	16.4 MB

    # Others
        1. simplify - 36 ms	15.6 MB
            pre, cur = None, head

            while cur:
                cur.next, pre, cur = pre, cur, cur.next

            return pre

        2. recursion - 32 ms 18.8 MB	
            if not head: return head
            if not head.next: return head

            orig_head = self.reverseList(head.next) 

            head.next.next = head
            head.next = None 

            return orig_head
"""