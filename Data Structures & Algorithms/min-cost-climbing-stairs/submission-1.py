class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        # def func(i):
        #     if i==n or i==n+1:
        #         return 0
        #     return cost[i]+min(func(i+1),func(i+2))
        dp=[-1]*(n+2)
        dp[n+1]=0
        dp[n]=0
        for i in range(n-1,-1,-1):
            dp[i]=cost[i]+min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])


        # return min(func(0),func(1))
        