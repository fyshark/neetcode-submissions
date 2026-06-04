# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: return 0

            return 1 + max(dfs(node.left), dfs(node.right))
        
        if not root: return 0
        diameter_current_node = dfs(root.left) + dfs(root.right)
        diameter_left_subtree = self.diameterOfBinaryTree(root.left)
        diameter_right_subtree = self.diameterOfBinaryTree(root.right)
        diameter_current_subtree = max(diameter_left_subtree, diameter_right_subtree)

        return max(diameter_current_node, diameter_current_subtree)