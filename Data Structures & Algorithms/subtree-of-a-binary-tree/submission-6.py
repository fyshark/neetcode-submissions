# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSametree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val and isSametree(p.left, q.left) and isSametree(p.right, q.right):
                return True
        
        if not root and subRoot:
            return False
        if not subRoot:
            return True
        if isSametree(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)