class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        max_area = 0
        
        def dfs(grid, visited, i, j):
            m, n = len(grid), len(grid[0])
            area = 1
            stack = [(i, j)]
            visited[i][j] = True

            while stack:
                r, c = stack.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and not visited[nr][nc]:
                        area += 1
                        visited[nr][nc] = True
                        stack.append((nr, nc))
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(dfs(grid, visited, i, j), max_area)
                    visited[i][j] = True
        return max_area