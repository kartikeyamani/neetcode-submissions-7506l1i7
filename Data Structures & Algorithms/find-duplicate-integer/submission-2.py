class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## We must use floyd's cycle detection algorithm
        fast=nums[0]
        slow=nums[0]
        while True:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if fast==slow:
                break
        fast=nums[0]
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]
        return fast