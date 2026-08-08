class Solution {
    private int ROWS, COLS;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();

        if (heights == null || heights.length == 0) {
            return res;
        }

        ROWS = heights.length;
        COLS = heights[0].length;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {

                boolean[] reached = new boolean[2];
                boolean[][] visited = new boolean[ROWS][COLS];

                dfs(heights, r, c, visited, reached);

                if (reached[0] && reached[1]) {
                    res.add(Arrays.asList(r, c));
                }
            }
        }

        return res;
    }

    private void dfs(int[][] heights, int r, int c,
                     boolean[][] visited,
                     boolean[] reached) {

        if (visited[r][c]) return;

        visited[r][c] = true;

        // Pacific
        if (r == 0 || c == 0) {
            reached[0] = true;
        }

        // Atlantic
        if (r == ROWS - 1 || c == COLS - 1) {
            reached[1] = true;
        }

        int[][] dirs = {
            {1, 0}, {-1, 0},
            {0, 1}, {0, -1}
        };

        for (int[] d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];

            if (nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS)
                continue;

            // Water flows downhill
            if (heights[nr][nc] <= heights[r][c]) {
                dfs(heights, nr, nc, visited, reached);
            }
        }
    }
}