class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False

        s1_sorted = sorted(s1)
        for i in range(len(s2)):
            window = s2[i:i+m]
            if sorted(window) == s1_sorted: 
                return True
        
        return False