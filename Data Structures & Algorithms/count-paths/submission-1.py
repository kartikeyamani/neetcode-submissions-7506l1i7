class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def func(i,j):
        #     if i<0 or j<0:
        #         return 0
        #     if i==0 or j==0:
        #         return 1
        #     return func(i-1,j)+func(i,j-1)
        # return func(m-1,n-1)\
        dp=[[0]*n]*m
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        