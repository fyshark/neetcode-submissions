class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();

        for (int[] interval: intervals) {
            int x = interval[0];
            int y = interval[1];

            if (newInterval[0] > y) {
                res.add(new int[]{x, y});
            } else if (newInterval[1] < x) {
                res.add(newInterval);
                newInterval = new int[]{x, y};
            } else {
                newInterval[0] = Math.min(x, newInterval[0]);
                newInterval[1] = Math.max(y, newInterval[1]);
            }
        }
        res.add(newInterval);
        return res.toArray(new int[res.size()][]);
    }
}
