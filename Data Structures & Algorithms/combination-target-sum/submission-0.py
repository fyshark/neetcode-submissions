class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []

        def backtrack(start, total):
            if total == target:
                res.append(comb[:])
                return
            
            if start >= len(nums) or total > target:
                return
            
            comb.append(nums[start])
            backtrack(start, total + nums[start])
            comb.pop()
            backtrack(start + 1, total)
        
        backtrack(0, 0)
        return res