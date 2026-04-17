class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        candidates.sort()

        def backtrack(start, total):
            if target == total:
                res.append(comb[:])
                return
            
            if target < total:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                comb.pop()
            
        backtrack(0, 0)
        return res