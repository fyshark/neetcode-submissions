class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for x, y in intervals:
            if newInterval[0] > y:
                res.append([x, y])
            elif newInterval[1] < x:
                res.append(newInterval)
                newInterval = [x, y]
            else:
                newInterval[0] = min(x, newInterval[0])
                newInterval[1] = max(y, newInterval[1])
        res.append(newInterval)
        return res