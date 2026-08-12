class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<n; i++) {
            graph.add(new ArrayList<>());
        }

        boolean[] visited = new boolean[n];
        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        int counter = 0;
        for (int i=0; i<n; i++) {
            if (!visited[i]) {
                dfs(graph, visited, i);
                counter++;
            }
        }
        return counter;
    }

    private void dfs(List<List<Integer>> graph, boolean[] visited, int curr) {
        if (visited[curr]) return;

        visited[curr] = true;

        for (int neighbor: graph.get(curr)) {
            dfs(graph, visited, neighbor);
        }
    }
}
