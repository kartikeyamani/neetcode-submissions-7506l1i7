class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(temp,i):
            if i==len(nums):
                res.append(temp.copy())
                return
            dfs(temp,i+1)
            temp.append(nums[i])
            dfs(temp,i+1)
            temp.pop(-1)
        dfs([],0)
        return res
            



                



        