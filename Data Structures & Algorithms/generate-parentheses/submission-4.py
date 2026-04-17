class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s):
            open = 0

            for c in s:
                if c == "(":
                    open += 1
                else:
                    open -= 1
                if open < 0:
                    return False
            return not open
        
        def backtrack(s):
            if 2 * n == len(s):
                if isValid(s):
                    res.append(s)
                return
        
            backtrack(s + "(")
            backtrack(s + ")")
        backtrack("")
        return res
