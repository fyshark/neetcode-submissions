class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(heights, visited, r, c):
            m, n = len(heights), len(heights[0])
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                    dfs(heights, visited, nr, nc)
        
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        for r in range(m):
            dfs(heights, pacific, r, 0)
            dfs(heights, atlantic, r, n-1)
        for c in range(n):
            dfs(heights, pacific, 0, c)
            dfs(heights, atlantic, m-1, c)
        
        return [list(cell) for cell in pacific & atlantic]