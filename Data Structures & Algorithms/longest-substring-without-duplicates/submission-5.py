class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        curr = set()

        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            length = max(length, r - l + 1)

        return length