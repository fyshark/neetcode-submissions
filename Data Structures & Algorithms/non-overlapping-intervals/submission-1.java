class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int counter = 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int[] curr = intervals[0];

        for (int i=1; i<intervals.length; i++) {
            int s = intervals[i][0];
            int e = intervals[i][1];
            if (s < curr[1]) {
                curr[1] = Math.min(curr[1], e);
                counter++;
            } else {
                curr[0] = s;
                curr[1] = e;
            }
        }
        return counter;
    }
}
