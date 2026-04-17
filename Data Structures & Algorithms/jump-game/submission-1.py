class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0

        for i in range(len(nums)):
            if max_i < i:
                return False
            curr_i = nums[i] + i
            max_i = max(max_i, curr_i)
        
        return max_i >= len(nums) - 1