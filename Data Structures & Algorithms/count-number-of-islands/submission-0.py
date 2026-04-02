class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=[0]
        def dfs(i,j):
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[i])-1:
                return 0
            if grid[i][j]!="1":
                return 0
            grid[i][j]="-1"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res[0]=res[0]+dfs(i,j)
        return res[0]



            
        