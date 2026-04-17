# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) >= 0
    
    def getHeight(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left, right = self.getHeight(root.left), self.getHeight(root.right)
        if left < 0 or right < 0:
            return -1
        if abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1