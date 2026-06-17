"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row, col, size):
            if self.isUniform(grid, row, col, size):
                return Node(
                    grid[row][col] == 1,
                    True,
                    None,
                    None,
                    None,
                    None
                )
            half = size // 2
            topLeft = dfs(row, col, half)
            topRight = dfs(row, col+half, half)
            bottomLeft = dfs(row+half, col, half)
            bottomRight = dfs(row+half, col+half, half)
        
            return Node(
                True,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )
        return dfs(0, 0, len(grid))

    def isUniform(self, grid, row, col, size):
        val = grid[row][col]

        for i in range(row, row+size):
            for j in range(col, col+size):
                if grid[i][j] != val:
                    return False
        return True