class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        idx = 0
        for color in range(3):
            freq = count.get(color, 0)
            nums[idx: idx+freq] = [color] * freq
            idx += freq
