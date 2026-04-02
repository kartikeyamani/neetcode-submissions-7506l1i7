class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        tdict={}
        for x in t:
            tdict[x]=tdict.get(x,0)+1
        i=0
        j=0
        sdict={}
        res=[]
        while j<len(s):
            sdict[s[j]]=sdict.get(s[j],0)+1
            ##All elements in tdict exists in sdict
            flag=0
            for ch in tdict:
                if ch not in sdict:
                    flag=1
                    break
                elif tdict[ch]>sdict[ch]:
                    flag=1
                    break
                else:
                    continue
            if flag==0:
                while i<=j:
                    if len(res)==0:
                        res.append(i)
                        res.append(j)
                    if len(res)!=0 and res[1]-res[0]>(j-i):
                        res[0]=i
                        res[1]=j
                    sdict[s[i]]=sdict.get(s[i],0)-1
                    if sdict[s[i]]==0:
                        del sdict[s[i]]
                    i+=1
                    flag1=0
                    for ch in tdict:
                        if ch not in sdict:
                            flag1=1
                            break
                        elif tdict[ch]>sdict[ch]:
                            flag1=1
                            break
                        else:
                            continue
                    if flag1==1:
                        break
            j+=1
        if len(res)==0:
            return ""
        return s[res[0]:res[1]+1]
            




        