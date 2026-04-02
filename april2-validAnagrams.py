class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(t)
        for i in range(len(s)):
            if s[i] in l1:
                l1.remove(s[i])
            else:
                return False
        if len(l1) == 0:
            return True
        else:
            return False
