class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26
        l = 0
        if len(s1) > len(s2): return False

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == s2_count: return True

        for r in range(len(s1), len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s2_count == s1_count:
                return True
        
        return False