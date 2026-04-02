class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1,count2={},{}
        for i in range(len(t)):
            count2[t[i]]=1+count2.get(t[i],0)
            count1[t[i]]=0
        have=0
        need=len(count2)
        n=len(s)
        res,reslen=[-1,-1],float("inf")
        l=0
        for r in range(n):
            if s[r] in count1:
                count1[s[r]]+=1
                if count1[s[r]]==count2[s[r]]:
                    have+=1
                while have==need:
                    if reslen>(r-l+1):
                        reslen=(r-l+1)
                        res[0]=l
                        res[1]=r
                    if s[l] in count1:
                        count1[s[l]]-=1
                        if count1[s[l]]<count2[s[l]]:
                            have-=1
                    l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""
                




        