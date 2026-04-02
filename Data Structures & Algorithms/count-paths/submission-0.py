class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def func(i,j):
            if i<0 or j<0:
                return 0
            if i==0 or j==0:
                return 1
            return func(i-1,j)+func(i,j-1)
        return func(m-1,n-1)
        