"""
    226. Invert Binary Tree
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node: TreeNode):
            if not node: return
            
            node.left, node.right = node.right, node.left
            
            invert(node.left) 
            invert(node.right)
        
        invert(root)

        return root

"""
    - 32 ms 14.2 MB

    - # Others
        1. BFS - 28 ms 14.4 MB
            def invertTree(self, root: TreeNode) -> TreeNode:
                if not root: return root

                dq = collections.deque([root])

                while dq:
                    node = dq.popleft()

                    node.right, node.left = node.left, node.right

                    dq.extend([child for child in [node.right, node.left] if child])

                return root
"""