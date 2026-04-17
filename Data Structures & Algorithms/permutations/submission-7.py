class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, comb = [], []
        used = [False] * len(nums)

        def backtrack(start):
            if start == len(nums):
                res.append(comb[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                comb.append(nums[i])
                used[i] = True
                backtrack(start + 1)
                comb.pop()
                used[i] = False
        backtrack(0)
        return res