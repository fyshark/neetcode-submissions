class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, k) -> bool:
            if k == len(word):
                return True

            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in visited or board[r][c] != word[k]:
                return False
            
            visited.add((r, c))
            res = backtrack(r+1, c, k+1) or backtrack(r-1, c, k+1) or backtrack(r, c+1, k+1) or backtrack(r, c-1, k+1)
            visited.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
        