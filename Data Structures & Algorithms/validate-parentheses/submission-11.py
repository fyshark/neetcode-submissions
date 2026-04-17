class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in mapping and stack:
                if stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True