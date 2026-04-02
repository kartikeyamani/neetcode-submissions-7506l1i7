class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j):
            if i>=ROWS or j>=COLS or i<0 or j<0 or grid[i][j]==0:
                return 0
            grid[i][j]=0
            area=0
            for dr,dc in directions:
                area+=dfs(i+dr,j+dc)
            return area+1
        maxvalue=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    maxvalue=max(maxvalue,dfs(r,c))
        return maxvalue