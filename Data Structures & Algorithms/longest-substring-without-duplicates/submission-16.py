class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        n=len(s)
        alpha={}
        maxlen=0
        while l<n and r<n:
            if s[r] not in alpha:
                alpha[s[r]]=r
            else:
                newl=alpha[s[r]]+1
                for k in range(l,newl):
                    del alpha[s[k]]
                alpha[s[r]]=r
                l=newl
            maxlen=max(maxlen,r-l+1)
            r+=1
            
        return maxlen
            




        