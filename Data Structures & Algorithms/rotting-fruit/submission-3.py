class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        fresh=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
                
        steps=0
        while q and fresh>0:
            size=len(q)
            for _ in range(size):
                r,c=q.popleft()
                for dr,dc in directions:
                    if 0<=r+dr<ROWS and 0<=c+dc<COLS and grid[r+dr][c+dc]==1:
                        q.append((r+dr,c+dc))
                        grid[r+dr][c+dc]=2
                        fresh-=1
            steps+=1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    return -1
        return steps

            

        

        