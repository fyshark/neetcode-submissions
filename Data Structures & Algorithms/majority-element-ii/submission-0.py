class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elementMap = Counter(nums)
        res = []

        for num, count in elementMap.items():
            if count > len(nums) // 3:
                res.append(num)
        
        return res