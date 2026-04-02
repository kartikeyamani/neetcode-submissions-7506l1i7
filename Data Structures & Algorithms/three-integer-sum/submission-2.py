class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        for i in range(0,len(nums)):
            twosum= 0-nums[i]
            newset=set()
            for j in range(i+1,len(nums)):
                newval=twosum-nums[j]
                if newval not in newset:
                    newset.add(nums[j])
                else:
                    res.add(tuple(sorted([nums[i],newval,nums[j]])))
                    newset.add(nums[j])
        return [list(t) for t in res]
        
                


        