class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(temp,index):
            if index>len(nums):
                return
            if index==len(nums):
                res.append(temp.copy())
                return
            
            temp.append(nums[index])
            dfs(temp,index+1)
            temp.pop()

            while index+1<=len(nums)-1 and nums[index]==nums[index+1]:
                index+=1
            dfs(temp,index+1)
        dfs([],0)

        return res

                



        