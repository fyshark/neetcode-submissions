class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            sum_ += nums[i]
            max_sum = max(max_sum, sum_)
            if sum_ < 0:
                sum_ = 0
            
        return max_sum