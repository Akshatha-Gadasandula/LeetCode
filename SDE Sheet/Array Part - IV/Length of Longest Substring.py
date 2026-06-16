class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        l= []
        for i in range(len(s)):
            if s[i] not in l:
                count = count +1
                l.append(s[i])
            else:
                max_count = max(count,max_count)
                l =  l[l.index(s[i])+1:]
                l.append(s[i])
                count = len(l)
        return max(count,max_count)

        
