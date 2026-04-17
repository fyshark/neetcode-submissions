class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sum_ = sum(nums[i:j+1])
                max_sum = max(max_sum, sum_)
        
        return max_sum