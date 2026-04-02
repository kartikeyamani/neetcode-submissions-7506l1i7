class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        s1dict={}
        for i in s1:
            s1dict[i]=s1dict.get(i,0)+1
        
        s2dict={}
        for j in range(0,len(s1)):
            s2dict[s2[j]]=s2dict.get(s2[j],0)+1
        if s1dict==s2dict:
            return True
        j=len(s1)
        i=0
        while j<len(s2):
            s2dict[s2[j]]=s2dict.get(s2[j],0)+1
            if s2dict[s2[i]]==1:
                del s2dict[s2[i]]
            else:
                s2dict[s2[i]]-=1
            if s1dict==s2dict:
                return True
            i+=1
            j+=1
            
        return False
            

        