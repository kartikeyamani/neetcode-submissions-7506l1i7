class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        # def func(i):
        #     if i==n-1:
        #         return nums[n-1]
        #     if i==n-2:
        #         return nums[n-2]
        #     cost=nums[i]
        #     for j in range(i+2,n):
        #         cost=max(cost,nums[i]+func(j))
        #     return cost
        # maxrob=float("-inf")
        # for i in range(0,n):
        #     maxrob=max(maxrob,func(i))
        # dp=[0]*(n)
        # dp[n-1]=nums[n-1]
        # dp[n-2]=nums[n-2]
        # maxtillhere=[float("-inf")]*(n)
        # maxtillhere[n-1]=nums[n-1]
        # for i in range(n-3,-1,-1):
        #     dp[i]=nums[i]+maxtillhere[i+2]
        #     maxtillhere[i+1]=max(maxtillhere[i+2],dp[i+1])
        # return max(maxtillhere[1],dp[0])
        # def func(i):
        #     if i>=len(nums):
        #         return 0
        #     pick=nums[i]+func(i+2)
        #     notpick=0+func(i+1)

        #     return max(pick,notpick)
        # return func(0)

        dp=[0]*(n)
        dp[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            pick=nums[i]
            if i!=n-2:
                pick+=dp[i+2]
            notpick=0+dp[i+1]
            dp[i]=max(pick,notpick)
        return dp[0]
        


        