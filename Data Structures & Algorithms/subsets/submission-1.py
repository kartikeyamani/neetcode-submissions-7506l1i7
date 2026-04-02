class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def func(i,temp):
            if i==len(nums):
                res.append(temp.copy())
                return
            func(i+1,temp)
            temp.append(nums[i])
            func(i+1,temp)
            temp.pop()
        func(0,[])
        return res

        