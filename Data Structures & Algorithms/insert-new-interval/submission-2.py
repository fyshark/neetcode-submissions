class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for x, y in intervals:
            if x > newInterval[1]:
                res.append(newInterval)
                newInterval = [x, y]
            elif y < newInterval[0]:
                res.append([x, y])
            else:
                newInterval[0] = min(newInterval[0], x)
                newInterval[1] = max(newInterval[1], y)
        res.append(newInterval)
        return res