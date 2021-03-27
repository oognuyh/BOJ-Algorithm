"""
    328. Odd Even Linked List
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head

        cur = head
        cur_even_nodes = even_nodes = ListNode()

        while cur and cur.next:
            cur_even_nodes.next = ListNode(cur.next.val)
            
            cur.next = cur.next.next 

            cur_even_nodes = cur_even_nodes.next
            cur = cur.next if cur.next else cur

        cur.next = even_nodes.next

        return head
        
"""
    - 32 ms	16.1 MB

    # Others
        1. two pointers - 36 ms	16.3 MB
            if head == None or head.next == None: return head
            odd = head
            even = head.next
            x = even.next 
            
            while x:
                temp = x
                even.next = x.next
                even = even.next
                
                temp.next = odd.next
                odd.next = temp
                odd = odd.next
                
                x= even.next if even else None
                
            return head
"""