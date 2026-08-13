# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = {}
        def lO(root, lvl):
            if root:
                level[lvl] = level.get(lvl, [])
                level[lvl].append(root.val)
                lO(root.left, lvl + 1)
                lO(root.right, lvl + 1)
        
        lO(root, 0)

        res = []
        for arr in level.values():
            res.append(arr)
        
        return res