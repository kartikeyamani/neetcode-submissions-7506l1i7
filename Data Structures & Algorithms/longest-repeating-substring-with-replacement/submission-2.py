class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        maxlen=0
        newdict={}
        while j<len(s):
            newdict[s[j]]=newdict.get(s[j],0)+1
            sorted_freq = sorted(newdict.items(), key=lambda x: x[1], reverse=True)
            mostfreqcount=sorted_freq[0][1]
            substringlength=j-i+1
            var=substringlength-mostfreqcount
            if var > k:
                newdict[s[i]]=newdict.get(s[i],0)-1
                if newdict[s[i]]==0:
                    del newdict[s[i]]
                i+=1
            else:
                maxlen=max(maxlen,j-i+1)
            j+=1
        return maxlen

        