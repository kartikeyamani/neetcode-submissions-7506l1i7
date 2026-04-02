class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newset=set()
        res=0
        for i in nums:
            newset.add(i)
        for i in nums:
            if i-1 not in newset:
                count=1
                val=i+1
                while val in newset:
                    count+=1
                    val+=1
                res=max(res,count)
        
        return res
                 