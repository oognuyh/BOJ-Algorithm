"""
    105. Construct Binary Tree from Preorder and Inorder Traversal
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])
            
            return node

"""
    - 124 ms 52.6 MB

    # Others
        1. dict - 48 ms 18.4 MB
            def buildTree(self, preorder, inorder):
                inorder_map = {val: i for i, val in enumerate(inorder)}
                
                return self.dfs_helper(inorder_map, preorder, 0, len(inorder) - 1)

            def dfs_helper(self, inorder_map, preorder, left, right):
                if not preorder : return
                
                node = preorder.pop(0)
                root = TreeNode(node)
                root_index = inorder_map[node]

                if root_index != left:
                    root.left = self.dfs_helper(inorder_map, preorder, left, root_index - 1)
                if root_index != right:
                    root.right = self.dfs_helper(inorder_map, preorder, root_index + 1, right)

                return root
"""