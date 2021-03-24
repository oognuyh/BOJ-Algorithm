"""
    21. Merge Two Sorted Lists
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2): return None
        
        merged_nodes = ListNode()
        
        cur_one = l1
        cur_another = l2
        cur_merged_nodes = merged_nodes
        
        while cur_one or cur_another:
            if cur_one and cur_another:
                if cur_one.val < cur_another.val:
                    cur_merged_nodes.val = cur_one.val
                    cur_one = cur_one.next
                else:
                    cur_merged_nodes.val = cur_another.val
                    cur_another = cur_another.next
                
                cur_merged_nodes.next = ListNode()
                cur_merged_nodes = cur_merged_nodes.next                       
            else:
                cur_merged_nodes.val = cur_one.val if not cur_another else cur_another.val
                cur_merged_nodes.next = cur_one.next if not cur_another else cur_another.next
                break
                
        return merged_nodes        

"""
    - 32 ms	14.4 MB	

    # Others
        1. simplify - 28 ms 14 MB
            if not l1 or not l2:
                return l1 or l2
        
            d = c = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    c.next = l1
                    l1 = l1.next
                else:
                    c.next = l2
                    l2 = l2.next
                c = c.next
                
            if l1 or l2:
                c.next = l1 or l2
            
            return d.next

        2. recursion - 32 ms 14.2 MB
            def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
                if not l1: return l2
                if not l2: return l1
                if l1.val <= l2.val:
                    l1.next = self.mergeTwoLists(l1.next, l2)
                    return l1
                if l1.val > l2.val:
                    l2.next = self.mergeTwoLists(l1, l2.next)
                    return l2

    # Tips
        1. return a variable with compare operator
            e.g. 
                if not l1 or not l2:
                    return l1 or l2
        2. initialize a variable while declaring another
            e.g. 
                d = c = ListNode(0)
"""