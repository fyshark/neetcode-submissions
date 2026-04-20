class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        count = 0
        prefixsum = 0

        for num in nums:
            prefixsum += num
            if prefixsum - k in prefix_map:
                count += prefix_map[prefixsum - k]
            prefix_map[prefixsum] = prefix_map.get(prefixsum, 0) + 1
        
        return count