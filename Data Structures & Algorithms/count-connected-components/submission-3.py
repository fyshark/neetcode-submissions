class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        dfs(0)

        return count