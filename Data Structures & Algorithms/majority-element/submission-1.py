class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        for val in counter:
            if counter[val] > len(nums) // 2:
                return val