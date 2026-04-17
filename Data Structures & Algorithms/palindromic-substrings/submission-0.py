class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def expand(s, left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(len(s)):
            res += expand(s, i, i)
            res += expand(s, i, i+1)
        return res