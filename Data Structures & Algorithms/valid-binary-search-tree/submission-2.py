# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTRange(node, minimum=None, maximum=None):
            if not node:
                return True   
            if maximum is not None and node.val >= maximum:
                return False
            if minimum is not None and node.val <= minimum:
                return False

            if node.left and not isValidBSTRange(node.left, minimum, node.val):
                return False
            if node.right and not isValidBSTRange(node.right, node.val, maximum):
                return False
            
            return True
        
        return isValidBSTRange(root)
