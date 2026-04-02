class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=float("-inf")
        def dfs(i,j):
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[i])-1:
                return 0
            if grid[i][j]!=1:
                return 0
            grid[i][j]=-1
            return 1+dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxarea=max(maxarea,dfs(i,j))
        return maxarea

        