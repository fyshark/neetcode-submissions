class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        sorted_map = sorted(nums_map.items(), key=lambda x: x[1], reverse=True)
        
        return [num for num, freq in sorted_map[:k]]