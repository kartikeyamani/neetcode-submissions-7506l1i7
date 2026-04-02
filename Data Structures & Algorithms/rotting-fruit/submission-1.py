class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        finaltime=0
        def bfs():
            queue=[]
            for r in range(0,len(grid)):
                for c in range(0,len(grid[0])):
                    if grid[r][c]==2:
                        queue.append(((r,c),0))
            latesttime=0
            while queue:
                newpair=queue.pop(0)
                row=newpair[0][0]
                col=newpair[0][1]
                for dr,dc in directions:
                    if row+dr<ROWS and col+dc<COLS and row+dr>=0 and col+dc>=0 and grid[row+dr][col+dc]==1:
                        newtime=newpair[1]+1
                        queue.append(((row+dr,col+dc),newtime))
                        grid[row+dr][col+dc]=2
                        latesttime=newtime
            return latesttime
        finaltime=bfs()
        for r in range(0,len(grid)):
            for c in range(0,len(grid[0])):
                if grid[r][c]==1:
                    return -1
        
        return finaltime


                
        