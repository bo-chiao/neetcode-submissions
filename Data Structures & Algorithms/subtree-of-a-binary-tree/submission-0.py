# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True

        l_is_subtree, r_is_subtree = False, False
        if root.left:
            l_is_subtree = self.isSubtree(root.left, subRoot)
        if root.right:
            r_is_subtree = self.isSubtree(root.right, subRoot)

        return l_is_subtree or r_is_subtree
