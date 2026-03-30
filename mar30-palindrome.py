class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        l,r = 0,len(str1)-1
        while l<r:
            if str1[l]!=str1[r]:
                return False
            l = l+1
            r = r-1
        return True
        
        
