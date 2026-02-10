# Divide Two INtegers
# Problem Number - 29
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        ans=0
        if dividend<0 and divisor <0:
            ans=dividend//divisor
        elif dividend<0 or divisor<0:
            b=-(dividend)//divisor 
            ans= -b
        else:
            ans=dividend//divisor 
        return min(INT_MAX, max(INT_MIN, ans))


        
