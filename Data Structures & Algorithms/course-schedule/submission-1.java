class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        int counter = 0;
        for (int i=0; i<numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        int[] inDegree = new int[numCourses];
        for (int[] edge: prerequisites) {
            int child = edge[0];
            int parent = edge[1];
            inDegree[child]++;
            graph.get(parent).add(child);
        }
        Queue<Integer> sources = new LinkedList<>();
        for (int i=0; i<numCourses; i++) {
            if (inDegree[i] == 0) {
                sources.offer(i);
            }
        }

        while (!sources.isEmpty()) {
            int course = sources.poll();
            counter++;
            for (int child: graph.get(course)) {
                inDegree[child]--;

                if (inDegree[child] == 0) {
                    sources.offer(child);
                }
            }
        }
        return counter == numCourses;
    }
}
