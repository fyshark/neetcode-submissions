class Solution {
    public boolean validTree(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[n];
        if (hasCycle(graph, visited, 0, -1)) return false;

        for (int i=0; i<n; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }

    boolean hasCycle(List<List<Integer>> graph, boolean[] visited, int curr, int parent) {
        visited[curr] = true;

        for (int neighbor: graph.get(curr)) {
            if ((visited[neighbor] && parent != neighbor) ||
                (!visited[neighbor] && hasCycle(graph, visited, neighbor, curr))) {
                return true;
            }
        }
        return false;
    }
}
