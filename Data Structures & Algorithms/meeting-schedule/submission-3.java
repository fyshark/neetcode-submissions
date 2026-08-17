/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        if (intervals.size() == 0) return true;
        intervals.sort((a, b) -> Integer.compare(a.start, b.end));
        Interval curr = intervals.get(0);
        for (int i=1; i<intervals.size(); i++) {
            int s = intervals.get(i).start;
            int e = intervals.get(i).end;

            if (s < curr.end) {
                return false;
            }
            curr = intervals.get(i);
        }
        return true;
    }
}
