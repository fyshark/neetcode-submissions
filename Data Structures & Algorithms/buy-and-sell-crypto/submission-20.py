class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for p in prices:
            if p > buy:
                max_profit = max(max_profit, p - buy)
            if p < buy:
                buy = p
        return max_profit