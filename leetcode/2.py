"""
    2. Add Two Numbers
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_nodes = cur_sum_nodes = ListNode()
        q = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            q, r = divmod(l1_val + l2_val + q, 10)
            cur_sum_nodes.next = ListNode(r)

            cur_sum_nodes = cur_sum_nodes.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if q:
                cur_sum_nodes.next = ListNode(q)
        
        return sum_nodes.next

"""
    - 64 ms	14.3 MB
"""