"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()
        q.append(node)
        vis = defaultdict()
        vis[node] = Node(node.val)
        
        while q:
            curr = q.popleft()
            for v in curr.neighbors:
                if v not in vis:
                    vis[v] = Node(v.val)
                    q.append(v)
                vis[curr].neighbors.append(vis[v])
        
        return vis[node]