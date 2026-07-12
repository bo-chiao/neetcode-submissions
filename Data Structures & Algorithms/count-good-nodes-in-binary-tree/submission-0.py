# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total_good_nodes = 0

        def dfs(node, max_num):
            if not node:
                return

            if node.val >= max_num:
                self.total_good_nodes += 1
                max_num = node.val

            if node.left:
                dfs(node.left, max_num)
            if node.right:
                dfs(node.right, max_num)

        dfs(root, -float("inf"))

        return self.total_good_nodes
        