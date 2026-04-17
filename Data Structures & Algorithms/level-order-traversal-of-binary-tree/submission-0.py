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

        depth = 0
        queue = deque()
        queue.append([root, depth])
        # key: depth, val: [(node1.val, node2.val,......]
        depth_map = defaultdict(list)
        while queue:
            node, depth = queue.popleft()
            depth_map[depth].append(node.val)

            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
        print(depth_map)
        return [depth_map[depth] for depth in sorted(depth_map)]