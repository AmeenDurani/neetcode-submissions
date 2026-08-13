# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSub(root, subRoot):
            if not root and not subRoot:
                return True
            if not root:
                return False
            if isSame(root, subRoot):
                return True
            return isSub(root.left, subRoot) or isSub(root.right, subRoot)

        def isSame(p, q):
            if not p and not q:
                return True
            elif bool(p) != bool(q):
                return False
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        return isSub(root, subRoot)
