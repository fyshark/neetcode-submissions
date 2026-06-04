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

            return max(dfs(node.left), dfs(node.right)) + 1
        
        if not root: return 0
        depth_current_node = dfs(root.left) + dfs(root.right)
        depth_left_subtree = self.diameterOfBinaryTree(root.left)
        depth_right_subtree = self.diameterOfBinaryTree(root.right)
        depth_current_subtree = max(depth_left_subtree, depth_right_subtree)

        return max(depth_current_node, depth_current_subtree)