class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif s[i] == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            elif s[i] == '*':
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMin < 0:
                leftMin = 0
            if leftMax < 0:
                return False
        
        return leftMin == 0