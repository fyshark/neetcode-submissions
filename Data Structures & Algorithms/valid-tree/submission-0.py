class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        visited.add(0)
        q = deque([0])
        while q:
            curr_node = q.popleft()
            for next_node in adj[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    q.append(next_node)
        
        return len(visited) == n