class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        distance=[]
        visited=[]
        N=len(grid)
        for i in range(len(grid)):
            distance.append([float("inf")]*len(grid[0]))
            visited.append([0]*len(grid[0]))
        hp=[[grid[0][0],0,0]]
        visited[0][0]=1
        while hp:
            time,row,col=heapq.heappop(hp)
            if row==len(grid)-1 and col==len(grid[0])-1:
                return time
            for dr,dc in [[0,1],[1,0],[-1,0],[0,-1]]:
                nr,nc=row+dr,col+dc
                if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0:
                    visited[nr][nc]=1
                    nexttime=max(time,grid[nr][nc])
                    heapq.heappush(hp,[nexttime,nr,nc])
                


            
            
            




        