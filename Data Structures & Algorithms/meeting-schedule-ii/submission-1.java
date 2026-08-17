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
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));
        PriorityQueue<Integer> rooms = new PriorityQueue<>();

        for (int i=0; i<intervals.size(); i++) {
            int start = intervals.get(i).start;
            int end = intervals.get(i).end;
            if (!rooms.isEmpty() && start >= rooms.peek()) {
                rooms.poll();
            }

            rooms.offer(end);
        }
        return rooms.size();
    }
}
