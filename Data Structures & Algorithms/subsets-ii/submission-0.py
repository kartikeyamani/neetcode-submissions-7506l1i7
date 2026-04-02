class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        nums.sort()
        def dfs(i):
            if i==len(nums):
                res.append(temp.copy())
                return
            
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
           
        dfs(0)
        return res
