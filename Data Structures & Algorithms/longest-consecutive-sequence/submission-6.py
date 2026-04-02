class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return 1
        maxcount=float("-inf")
        nums.sort()
        tempcount=1
        print(nums)
        for i in range(n-1):
            if nums[i+1]==nums[i]+1:
                tempcount+=1
                maxcount=max(maxcount,tempcount)
            elif nums[i+1]==nums[i]:
                maxcount=max(maxcount,tempcount)
            else:
                tempcount=1
                maxcount=max(maxcount,tempcount)
        return maxcount






        