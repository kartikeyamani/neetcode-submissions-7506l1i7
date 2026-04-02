class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(s,e):
            if s==e:
                return [nums[s]]
            mid=(s+e)//2
            list1=merge(s,mid)
            list2=merge(mid+1,e)
            i,j=0,0
            res=[]
            while i<len(list1) and j<len(list2):
                if list1[i]<=list2[j]:
                    res.append(list1[i])
                    i+=1
                else:
                    res.append(list2[j])
                    j+=1
                
            while i<len(list1):
                res.append(list1[i])
                i+=1
            while j<len(list2):
                res.append(list2[j])
                j+=1
            return res
        return merge(0,len(nums)-1)



        