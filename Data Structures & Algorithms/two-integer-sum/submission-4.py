class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(nums):
            my_dict[n] = i;
        
        for i, n in enumerate(nums):
            diff = target - nums[i]

            if diff in my_dict.keys() and my_dict[diff] != i:
                return sorted([i, my_dict[diff]])


