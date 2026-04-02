class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newdict={}
        l,r=0,0
        maxlength=0
        while l<len(s) and r<len(s):
            if s[r] in newdict:
                newl=newdict[s[r]]+1
                for k in range(l,newl):
                    del newdict[s[k]]
                l=newl
                newdict[s[r]]=r
                maxlength=max(maxlength,r-l+1)
            else:
                newdict[s[r]]=r
                maxlength=max(maxlength,r-l+1)
            r+=1
        return maxlength



