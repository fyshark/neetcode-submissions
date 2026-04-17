class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                q = deque([i])

            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        return count