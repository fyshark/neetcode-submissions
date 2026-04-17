class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for k in count:
            if count[k] == 1:
                return k