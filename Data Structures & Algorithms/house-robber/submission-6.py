class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1 for _ in range(len(nums))]
        def func(ind):
            if ind<0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            pick=nums[ind]+func(ind-2)
            notpick=func(ind-1)
            dp[ind]=max(pick,notpick)
            return dp[ind]
        return func(len(nums)-1)