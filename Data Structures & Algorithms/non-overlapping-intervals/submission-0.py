class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x: x[0])
        curr_x, curr_y = intervals[0]

        for start, end in intervals[1:]:
            if curr_y > start:
                curr_y = min(curr_y, end)
                res += 1
            else:
                curr_y = end
        return res