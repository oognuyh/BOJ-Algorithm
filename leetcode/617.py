"""
    617. Merge Two Binary Trees
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:            
            node = TreeNode(root1.val + root2.val)
            
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else:
            return root1 or root2

"""
    - 88 ms 15.7 MB
"""