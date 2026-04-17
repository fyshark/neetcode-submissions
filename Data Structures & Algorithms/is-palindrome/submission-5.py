class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb = ''
        for c in s:
            if c.isalnum():
                sb += c.lower()
        return sb == sb[::-1]