"""
    1038. Binary Search Tree to Greater Sum Tree
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            root.val = self.val = self.val + root.val
            self.bstToGst(root.left)
        
        return root

"""
    - 32 ms 14.3 MB
"""