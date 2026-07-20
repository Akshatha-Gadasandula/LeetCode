class Solution:

    def numberOfSpecialChars(self, s: str) -> int:

        l=[0]*26
        h=[0]*26

        vis=[True]*26

        for ch in s:

            if 'A'<=ch<='Z':

                idx=ord(ch)-ord('A')

                if l[idx]==0:
                    vis[idx]=False
                else:
                    h[idx]+=1

            else:

                idx=ord(ch)-ord('a')

                if h[idx]>0:
                    vis[idx]=False

                l[idx]+=1

        count=0

        for i in range(26):

            if not vis[i]:
                continue

            if l[i] and h[i]:
                count+=1

        return count
