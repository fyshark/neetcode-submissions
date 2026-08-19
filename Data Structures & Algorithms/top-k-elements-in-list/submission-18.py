class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        heap = []
        for num, freq in nums_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]