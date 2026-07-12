# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        NOT_BALANCED = -1

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            if left_depth == NOT_BALANCED:
                return NOT_BALANCED

            right_depth = dfs(node.right)
            if right_depth == NOT_BALANCED:
                return NOT_BALANCED 

            if abs(left_depth - right_depth) > 1:
                return NOT_BALANCED
            
            return 1 + max(left_depth, right_depth)
        
        return dfs(root) != NOT_BALANCED
