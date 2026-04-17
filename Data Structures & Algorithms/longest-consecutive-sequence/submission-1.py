class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_ = 0

        for num in set_nums:
            if num-1 not in set_nums:
                temp = num
                longest = 1
                while temp+1 in set_nums:
                    longest += 1
                    temp += 1
                max_ = max(longest, max_)
        
        return max_