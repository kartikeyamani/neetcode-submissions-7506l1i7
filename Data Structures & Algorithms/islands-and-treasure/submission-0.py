class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        INF=2147483647
        visited=set()
        q=deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited.add((i,j))
        while q:
            row,col=q.popleft()
            for r,c in directions:
                nr,nc=row+r,col+c
                if (0<=nr<ROWS and 0<=nc<COLS and \
                    (nr,nc) not in visited and grid[nr][nc]==INF):
                    visited.add((nr,nc))
                    grid[nr][nc]=grid[row][col]+1
                    q.append((nr,nc))
        





        