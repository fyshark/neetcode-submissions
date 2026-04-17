class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        self.comb = ""
        if not digits:
            return []

        def backtrack(start):
            if start == len(digits):
                res.append(self.comb)
                return
            
            for c in digits_map[digits[start]]:
                self.comb += c
                backtrack(start+1)
                self.comb = self.comb[:-1]

        backtrack(0)
        return res
            