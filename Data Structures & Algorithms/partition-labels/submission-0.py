class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = defaultdict(int)
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        
        start = 0
        end = 0
        res = []
        for i, val in enumerate(s):
            end = max(end, last_occurrence[val])

            if end == i:
                res.append(end - start + 1)
                start = end + 1
        
        return res