class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        newset=set()
        def dfs(i):
            if len(newset)==len(nums):
                res.append(temp.copy())
                return
            for j in range(len(nums)):
                if j in newset:
                    continue
                temp.append(nums[j])
                newset.add(j)
                dfs(i+1)
                temp.pop()
                newset.discard(j)
        dfs(0)
        return res



        