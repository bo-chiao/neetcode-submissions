# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_depth(self, node):
        if not node:
            return 0

        return 1 + max(self.max_depth(node.left), self.max_depth(node.right))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        diameter = self.max_depth(root.left) + self.max_depth(root.right)

        return max(diameter, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        
        