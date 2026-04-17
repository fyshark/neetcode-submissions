class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        current = 1
        longest = 1
        n = len(nums)

        if n == 0:
            return 0
        
        for i in range(1, n):
            if sorted_nums[i-1] == sorted_nums[i]:
                continue
            if sorted_nums[i-1] + 1 == sorted_nums[i]:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        
        return longest