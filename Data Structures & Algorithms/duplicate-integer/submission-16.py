class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}

        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        for num in nums_map:
            if nums_map[num] > 1:
                return True
        return False