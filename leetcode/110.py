"""
    110. Balanced Binary Tree
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root: TreeNode) -> int:
            if not root: return 0

            left, right = check(root.left), check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(root) != -1

"""
    - 36 ms	19.1 MB
"""