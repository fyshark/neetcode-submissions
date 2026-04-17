class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if not digits:
            return []

        def backtrack(start, curr):
            if start == len(digits):
                res.append(curr[:])
                return
            
            for c in digits_map[digits[start]]:
                backtrack(start+1, curr+c)
        backtrack(0, "")
        return res