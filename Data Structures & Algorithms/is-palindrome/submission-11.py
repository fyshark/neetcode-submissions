class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for c in s:
            if c.isalnum():
                new_s.append(c)
        
        l, r = 0, len(new_s) - 1
        while l<r:
            if new_s[l].lower() != new_s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True