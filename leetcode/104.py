"""
    104. Maximum Depth of Binary Tree
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0

        dq, depth = collections.deque([root]), 0
        
        while dq:
            depth += 1
            
            for _ in range(len(dq)):
                cur = dq.popleft()
                
                if cur.left:
                    dq.append(cur.left)
                
                if cur.right:
                    dq.append(cur.right)
                    
        return depth

"""
    - 40 ms 15.4 MB

    # Others
        1. recursion - 44 ms 16.1 MB
            def maxDepth(self, root: TreeNode) -> int:
                if root is None: return 0

                return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
"""