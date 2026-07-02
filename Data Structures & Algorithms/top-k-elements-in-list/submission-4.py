class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)

        for num in nums:
            nums_map[num] += 1
        
        arr = []

        for val, cnt in nums_map.items():
            arr.append([val, cnt])
        arr.sort(key=lambda x: x[1])

        res = []
        while len(res) < k:
            res.append(arr.pop()[0])
        
        return res
