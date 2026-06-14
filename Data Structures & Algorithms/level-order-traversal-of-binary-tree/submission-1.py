# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_map = {}
        queue = deque()
        queue.append([0, root])

        while queue:
            level, node = queue.popleft()
            if level not in level_map:
                level_map[level] = [node.val]
            else:
                level_map[level].append(node.val)
            
            if node.left:
                queue.append([level+1, node.left])
            if node.right:
                queue.append([level+1, node.right])
        
        return [level_map[level] for level in level_map]