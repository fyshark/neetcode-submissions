class Solution {
    private int ROWS, COLS;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        if (heights == null || heights.length == 0) return res;
        ROWS = heights.length;
        COLS = heights[0].length;

        boolean[][] pacific = new boolean[ROWS][COLS];
        boolean[][] atlantic = new boolean[ROWS][COLS];
        for (int r=0; r<ROWS; r++) {
            dfs(heights, pacific, r, 0);
            dfs(heights, atlantic, r, COLS-1);
        }

        for (int c=0; c<COLS; c++) {
            dfs(heights, pacific, 0, c);
            dfs(heights, atlantic, ROWS-1, c);
        }

        for (int r=0; r<ROWS; r++) {
            for (int c=0; c<COLS; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    res.add(Arrays.asList(r, c));
                }
            }
        }
        return res;
    }

    private void dfs(int[][] heights, boolean[][] visited, int r, int c) {
        if (visited[r][c]) return;

        visited[r][c] = true;
        int[][] dirs = {
            {1, 0}, {-1, 0},
            {0, 1}, {0, -1}
        };

        for (int[] d: dirs) {
            int nr = r+d[0];
            int nc = c+d[1];

            if (nr<0||nc<0||nr>=ROWS||nc>=COLS) {
                continue;
            }

            if (heights[nr][nc] >= heights[r][c]) {
                dfs(heights, visited, nr, nc);
            }
        }
    }
}
