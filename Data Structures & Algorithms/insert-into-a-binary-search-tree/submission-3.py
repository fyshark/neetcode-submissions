# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        target = TreeNode(val)
        head = root
        if not root:
            return target

        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = target
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = target
                    break
        return head