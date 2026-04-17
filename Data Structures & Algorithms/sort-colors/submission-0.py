class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        idx = 0
        for color in range(3):
            freq = count[color]
            nums[idx: idx+freq] = [color] * freq
            idx += freq
        