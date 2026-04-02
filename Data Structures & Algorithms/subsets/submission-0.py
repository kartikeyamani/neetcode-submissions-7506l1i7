class Solution:
    def subsets( self,nums: List[int]) -> List[List[int]]:
        res=[]
        finalist=[]
        def func(nums:List[int],i:int,finalist:List[int]):
            if len(nums)==i:
                res.append(finalist)
                return
            newlist=finalist.copy()
            func(nums,i+1,finalist)
            finalist=newlist
            finalist.append(nums[i])
            func(nums,i+1,finalist)
        func(nums,0,finalist)
        return res
            


        
        