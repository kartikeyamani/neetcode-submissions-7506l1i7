class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
        #print(board)
        col=set()
        posdiag=set()
        negdiag=set()
        def helper(r):
            if r==n:
                copy=["".join(row) for row in board]
                #print(1)
                res.append(copy)
                return
            for c in range(n):
                if (r-c) in negdiag or (r+c) in posdiag or c in col:
                    continue
                negdiag.add(r-c)
                posdiag.add(r+c)
                col.add(c)
                board[r][c]="Q"
                helper(r+1)
                board[r][c]="."
                negdiag.remove(r-c)
                posdiag.remove(r+c)
                col.remove(c)
        helper(0)
        return res




        
        






            
            

        