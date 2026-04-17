class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        count = 0
        
        def dfs(grid, visited, i, j):
            m, n = len(grid), len(grid[0])
            stack = [(i, j)]
            visited[i][j] = True

            while stack:
                r, c = stack.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1" and not visited[nr][nc]:
                        stack.append((nr, nc))
                        visited[nr][nc] = True
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(grid, visited, i, j)
                    count += 1
        return count