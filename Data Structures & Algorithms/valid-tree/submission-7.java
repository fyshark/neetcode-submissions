class Solution {
    int[] parent;
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n-1) {
            return false;
        }

        parent = new int[n];

        for (int i=0; i<n; i++) {
            parent[i] = i;
        }

        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];
            int rootU = find(u);
            int rootV = find(v);

            if (rootU == rootV) {
                return false;
            }
            parent[rootU] = rootV;
        }
        return true;
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
}
