class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[', '}':'{', ')':'('}
        stack = []
        for c in s:
            if c not in brackets:
                stack.append(c)
            else:
                if not stack or stack.pop() != brackets[c]:
                    return False
        
        return not stack