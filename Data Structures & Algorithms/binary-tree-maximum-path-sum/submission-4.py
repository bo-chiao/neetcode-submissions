# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")

        def max_subtree_sum(node):
            if not node:
                return 0

            left_subtree = max(max_subtree_sum(node.left), 0)
            right_subtree = max(max_subtree_sum(node.right), 0)

            nonlocal max_sum
            max_sum = max(
                left_subtree + node.val + right_subtree,
                max_sum,
            )

            return max(
                left_subtree + node.val,
                right_subtree + node.val,
            )

        max_subtree_sum(root)

        return max_sum
