class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newdict={}
        i=0
        j=i
        maxlen=0
        while j<len(s):
            if s[j] not in newdict:
                newdict[s[j]]=j
            else:
                newi=newdict[s[j]]+1
                for k in range(i,newi):
                    del newdict[s[k]]
                i=newi
                newdict[s[j]]=j
            maxlen=max(maxlen,j-i+1)
            j+=1
        return maxlen


        