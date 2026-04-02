class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def func(temp,totalsum,i):
            if totalsum==target:
                res.append(temp.copy())
                return
            if totalsum>target:
                return
            for j in range(i,len(nums)):
                temp.append(nums[j])
                func(temp,totalsum+nums[j],j)
                temp.pop()

        func([],0,0)
        return res

