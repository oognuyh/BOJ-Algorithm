"""
    543. Diameter of Binary Tree
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def search(parent: TreeNode) -> int:
            if not parent: return 0

            children = [search(parent.left), search(parent.right)]

            self.answer = max(self.answer, sum(children))

            return 1 + max(children)
        
        self.answer = 0
        
        search(root)

        return self.answer

"""
    - 52 ms 16.5 MB
"""