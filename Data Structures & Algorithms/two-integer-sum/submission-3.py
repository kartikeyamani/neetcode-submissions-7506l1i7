class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict={}
        for i in range(len(nums)):
            if target-nums[i] in newdict:
                return [newdict[target-nums[i]],i]
            
            newdict[nums[i]]=i
        return []


         
        