class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(temp,index,target):
            if target==0:
                res.append(temp.copy())
                return
            if target<0 or index>=len(nums):
                return
            dfs(temp,index+1,target)
            temp.append(nums[index])
            dfs(temp,index,target-nums[index])
            temp.pop()
        dfs([],0,target)
        return res

        