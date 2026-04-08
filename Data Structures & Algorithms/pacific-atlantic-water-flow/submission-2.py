class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # From the pacific cells do the dfs and find out if they can reach to 
        # atlantic ocean, from atlantic cells do dfs and see if they can reach to pacific.
        ROWS=len(heights)
        COLS=len(heights[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        pacific=set()
        atlantic=set()
        res=[]
        def dfs(i,j,visit,prevheight):
            if i>=ROWS or j>=COLS or i<0 or j<0 or (i,j) in visit or heights[i][j]<prevheight:
                return
            visit.add((i,j))
            for dr,dc in directions:
                dfs(i+dr,j+dc,visit,heights[i][j])
            

        for j in range(COLS):
            dfs(0,j,pacific,float("-inf"))
            dfs(ROWS-1,j,atlantic,float("-inf"))

        for i in range(ROWS):
            dfs(i,0,pacific,float("-inf"))
            dfs(i,COLS-1,atlantic,float("-inf"))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res
        

        