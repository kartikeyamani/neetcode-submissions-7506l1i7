class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(temp,s):
            if len(temp)==len(nums):
                res.append(temp.copy())
                return
            for i in range(len(nums)):
                if i not in s:
                    temp.append(nums[i])
                    s.add(i)
                    dfs(temp,s)
                    s.remove(i)
                    temp.pop()
        dfs([],set())
        return res
            
        