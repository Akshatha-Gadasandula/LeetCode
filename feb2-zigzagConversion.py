#Zig Zag Conversion
#Problem - 6
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=[]
        k=0
        for i in range(0,numRows):
            l.append("")
        i=0
        while(i<len(s)):

            if(k<numRows):

                l[k]=l[k]+s[i]
                k=k+1
                i=i+1

            else:
                for j in range(numRows-2,0,-1):
                    if i>=len(s):  
                        break
                    l[j]=l[j]+s[i]
                    i=i+1
           
                k=0
                
        s1=""
        for i in l:
            s1=s1+i


        return s1
