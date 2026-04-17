class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dfs(r+dr, c+dc)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'