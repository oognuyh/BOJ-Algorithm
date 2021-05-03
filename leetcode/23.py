"""
    23. Merge k Sorted Lists
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        hq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(hq, (lists[i].val, i, lists[i]))

        while hq:
            node = heapq.heappop(hq)
            idx, result.next = node[1], node[2]

            result = result.next
            if result.next:
                heapq.heappush(hq, (result.next.val, idx, result.next))
        
        return root.next

"""
    - 96 ms	18 MB

    # Others
        1. divide - 116 ms	17.7 MB
            def mergeKLists(self, lists):
                if not lists:
                    return None
                if len(lists) == 1:
                    return lists[0]
                mid = len(lists) // 2
                l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
                return self.merge(l, r)
            
            def merge(self, l, r):
                dummy = p = ListNode()
                while l and r:
                    if l.val < r.val:
                        p.next = l
                        l = l.next
                    else:
                        p.next = r
                        r = r.next
                    p = p.next
                p.next = l or r
                return dummy.next
            
            def merge1(self, l, r):
                if not l or not r:
                    return l or r
                if l.val< r.val:
                    l.next = self.merge(l.next, r)
                    return l
                r.next = self.merge(l, r.next)
                return r
"""