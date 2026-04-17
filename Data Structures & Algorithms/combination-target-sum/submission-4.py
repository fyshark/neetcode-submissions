class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []

        def backtrack(start, total):
            if target == total:
                res.append(comb[:])
                return
            
            if target < total:
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, total + nums[i])
                comb.pop()
        backtrack(0, 0)
        return res