class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        for i in range(0,len(s)):
            newset=set()
            for j in range(i,len(s)):
                if s[j] not in newset:
                    newset.add(s[j])
                else:
                    break
            maxlen=max(maxlen,len(newset))
        
        return maxlen
                

        