class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS=len(grid)
        COLS=len(grid[0])
        visited=set()
        q=deque()
        INF=2147483647
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    visited.add((i,j))
                    q.append((i,j))
        steps=0
        while q:
            size=len(q)
            
            for i in range(size):
                r,c=q.popleft()
                for dr,dc in directions:
                    if 0<=r+dr<ROWS and 0<=c+dc<COLS and grid[r+dr][c+dc]==INF:
                        grid[r+dr][c+dc]=steps+1
                        visited.add((r+dr,c+dc))
                        q.append((r+dr,c+dc))
            steps+=1
        



        

        