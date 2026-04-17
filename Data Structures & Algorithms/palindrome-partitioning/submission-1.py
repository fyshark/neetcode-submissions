class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def isPalindrome(sub):
            l, r = 0, len(sub)-1
            while l < r:
                if sub[l] == sub[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                if isPalindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return res
                

