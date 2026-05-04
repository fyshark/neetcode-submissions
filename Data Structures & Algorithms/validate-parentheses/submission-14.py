class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif not stack or brackets[stack.pop()] != c:
                return False
        
        return not stack