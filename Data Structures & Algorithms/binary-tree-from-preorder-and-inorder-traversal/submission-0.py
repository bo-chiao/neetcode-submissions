# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        val = preorder[0]

        node = TreeNode(val)
        split = inorder.index(val)

        node.left = self.buildTree(preorder[1 : split + 1], inorder[: split])
        node.right = self.buildTree(preorder[split + 1 :], inorder[split + 1 :])
        
        return node
