class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(n):
            if n < 2:
                return cost[n]
            if n in memo:
                return memo[n]
            memo[n] = cost[n] + min(dp(n-1), dp(n-2))
            return memo[n]
        
        length = len(cost)
        return min(dp(length-1), dp(length-2))