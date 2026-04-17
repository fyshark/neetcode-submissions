class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            daysNeeded, currWeights = 1, 0
            m = (l+r)//2
            for w in weights:
                if w + currWeights > m:
                    daysNeeded += 1
                    currWeights = 0
                currWeights += w

            if daysNeeded > days:
                l = m + 1
            else:
                r = m
        
        return l