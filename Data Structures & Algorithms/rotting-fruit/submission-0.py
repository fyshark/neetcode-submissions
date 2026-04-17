class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotted = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotted.append((i, j))
        
        minute = 0
        while rotted and fresh > 0:
            for _ in range(len(rotted)):
                r, c = rotted.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        rotted.append((nr, nc))
            minute += 1
        return -1 if fresh > 0 else minute