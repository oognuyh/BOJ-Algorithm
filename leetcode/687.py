"""
    687. Longest Univalue Path
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def search(node: TreeNode, previous: int) -> int:
            if not node: return 0
            
            left, right = search(node.left, node.val), search(node.right, node.val)
            self.maximum = max(self.maximum, left + right)
            
            return max(left, right) + 1 if node.val == previous else 0
            
        self.maximum = 0
        
        search(root, root.val) if root else False
        
        return self.maximum

"""
    - 348 ms 18.1 MB
"""