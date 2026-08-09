class Solution {
    private int ROWS, COLS;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        ROWS = heights.length;
        COLS = heights[0].length;
        if (heights == null || heights.length == 0) return res;
        
        for (int r=0; r<ROWS; r++) {
            for (int c=0; c<COLS; c++) {
                boolean[][] visited = new boolean[ROWS][COLS];
                boolean[] reached = new boolean[2];

                dfs(heights, visited, reached, r, c);
                if (reached[0] && reached[1]) {
                    res.add(Arrays.asList(r, c));
                }
            }
        }
        return res;
    }

    private void dfs(int[][] heights, boolean[][] visited, boolean[] reached, int r, int c) {
        if (visited[r][c]) return;
        
        int[][] dirs = {
            {1, 0}, {-1, 0},
            {0, 1}, {0, -1}
        };
        
        if (r == 0 || c == 0) {
            reached[0] = true;
        }

        if (r == ROWS-1 || c == COLS-1) {
            reached[1] = true;
        }

        visited[r][c] = true;
        for (int[] d: dirs) {
            int nr = r+d[0];
            int nc = c+d[1];

            if (nr<0||nc<0||nr>=ROWS||nc>=COLS) continue;
            if (heights[nr][nc] <= heights[r][c]) {
                dfs(heights, visited, reached, nr, nc);
            }
        }
    }
}
