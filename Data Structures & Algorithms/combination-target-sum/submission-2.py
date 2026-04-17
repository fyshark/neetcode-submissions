class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []

        def backtrack(start, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i, total + nums[i])
                comb.pop()
        backtrack(0, 0)
        return res
