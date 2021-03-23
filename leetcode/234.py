"""
    234. Palindrome Linked List
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur, nodes = head, []
        
        while cur:
            nodes.append(cur.val)
            cur = cur.next
            
        return nodes == nodes[::-1]

"""
    - 752 ms 47.1 MB	

    # Others
        1. deque - 824 ms 47.6 MB	
            q = collections.deque()
            node = head
            
            while node:
                q.append(node.val)
                node = node.next
                
            while len(q) > 1:
                if q.popleft() != q.pop():
                    return False
            return True
        
        2. two pointers - 876 ms 47.3 MB
            reverse, fast = None, head
            # Reverse the first half part of the list.
            while fast and fast.next:
                fast = fast.next.next
                head.next, reverse, head = reverse, head, head.next

            # If the number of the nodes is odd,
            # set the head of the tail list to the next of the median node.
            tail = head.next if fast else head

            # Compare the reversed first half list with the second half list.
            # And restore the reversed first half list.
            is_palindrome = True
            while reverse:
                is_palindrome = is_palindrome and reverse.val == tail.val
                reverse.next, head, reverse = head, reverse, reverse.next
                tail = tail.next

            return is_palindrome

    # Tips
        1. Big O of deque is O(1) when appending or popping from both the right and left side because the deque doesn't perform reallocation
        2. list is a better choice when accessing elements. (list: O(1), deque: O(n))
"""
