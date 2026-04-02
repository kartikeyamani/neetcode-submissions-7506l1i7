class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        res=[]
        for index,val in enumerate(nums):
            if (target-val) in dict1:
                res.append(dict1[target-val])
                res.append(index)
                return sorted(res)
            else:
                dict1[val]=index
         
        