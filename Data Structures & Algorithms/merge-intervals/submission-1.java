class Solution {
    public int[][] merge(int[][] intervals) {
        List<int []> res = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int[] curr = intervals[0];

        for (int i=1; i<intervals.length; i++) {
            int s = intervals[i][0];
            int e = intervals[i][1];

            if (s <= curr[1]) {
                curr[1] = Math.max(e, curr[1]);
            } else {
                res.add(new int[]{curr[0], curr[1]});
                curr = new int[]{s, e};
            }
        }
        res.add(curr);
        return res.toArray(new int[res.size()][]);
    }
}
