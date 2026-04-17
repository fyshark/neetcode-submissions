class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for x, y in intervals:
            if newInterval[1] < x:
                res.append(newInterval)
                newInterval = [x, y]
            elif newInterval[0] > y:
                res.append([x, y])
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
        res.append(newInterval)
        return res