class Solution {
    int[] parent;
    public int countComponents(int n, int[][] edges) {
        parent = new int[n];
        int counter = n;
        for (int i=0; i<n; i++) {
            parent[i] = i;
        }

        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];
            int rootU = find(u);
            int rootV = find(v);

            if (rootU != rootV) {
                parent[rootU] = rootV;
                counter--;
            }
        }
        return counter;
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
}
