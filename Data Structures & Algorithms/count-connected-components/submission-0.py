class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                q = deque([i])
                count += 1
            
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        
        return count