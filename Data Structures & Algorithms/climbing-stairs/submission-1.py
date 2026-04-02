class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def func(i):
            if i>n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            if i==n:
                return 1
            dp[i]=func(i+1)+func(i+2)
            return dp[i]
        return func(0)
        