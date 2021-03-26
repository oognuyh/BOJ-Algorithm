"""
    24. Swap Nodes in Pairs
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head
        
"""
    - 28 ms 14.3 MB

    # Others
        1. recursion - 32 ms 14.2 MB
            if not head or not head.next: return head
            
            next_node = head.next  # Get the 2nd value
            head.next = self.swapPairs(head.next.next) # It will return the pointer of every swaped nodes .ex: 1->2->3->4-None , 3->4 will get swap 1st and becomes 4->3. Finally it beomes 1->4>3
            next_node.next = head # We got the value of 2 previously, so we can point that to 1. It became 2->1->3->

            return next_node

        2. if is faster than compare operation(28 ms < 32 ms)
            e.g. 
                while cur and cur.next: -> while cur:
                                                if cur.next: pass
                                                else: pass
"""