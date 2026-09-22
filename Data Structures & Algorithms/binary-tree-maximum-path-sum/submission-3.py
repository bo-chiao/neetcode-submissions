# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        memo = {}
        max_sum = -float("inf")

        def max_subtree_sum(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            left_subtree = max_subtree_sum(node.left)
            right_subtree = max_subtree_sum(node.right)

            nonlocal max_sum
            max_sum = max(
                left_subtree + node.val + right_subtree,
                left_subtree + node.val,
                right_subtree + node.val,
                node.val,
                max_sum,
            )

            memo[node] = max(
                left_subtree + node.val,
                right_subtree + node.val,
                node.val,
            )

            return memo[node]

        max_subtree_sum(root)

        return max_sum
