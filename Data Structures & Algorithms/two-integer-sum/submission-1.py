class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict=dict()
        for i in range(len(nums)):
            var=target-nums[i]
            if var in new_dict:
                return [new_dict[var],i]
            else:
                new_dict[nums[i]]=i

        