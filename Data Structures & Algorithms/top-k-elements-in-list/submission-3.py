class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newdict={}
        for i in nums:
            newdict[i]=newdict.get(i,0)+1
        
        arr2=[[] for _ in range(len(nums)+1)]
        for key,val in newdict.items():
            arr2[val].append(key)
        res=[]
        for i in range(len(arr2)-1,-1,-1):
            if len(arr2[i])!=0:
                for num in arr2[i]:
                    res.append(num)
                    if len(res)==k:
                        return res




        