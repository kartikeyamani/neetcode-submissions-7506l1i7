class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        count1={}
        count2={}
        for i in range(n1):
            count1[s1[i]]=1+count1.get(s1[i],0)
            count2[s2[i]]=1+count2.get(s2[i],0)

        for i in range(n2-n1):
            if count2==count1:
                return True
            else:
                count2[s2[i]]-=1
                count2[s2[i+n1]]=1+count2.get(s2[i+n1],0)
                if count2[s2[i]]==0:
                    del count2[s2[i]]
        return count1==count2
            
        




        