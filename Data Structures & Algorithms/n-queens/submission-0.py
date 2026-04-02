class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        col=set()
        posdiag=set()
        negdiag=set()
        res=[]
        def dfs(i):
            if i==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c not in col and (i-c) not in negdiag and (i+c) not in posdiag:
                    board[i][c]="Q"
                    negdiag.add(i-c)
                    posdiag.add(i+c)
                    col.add(c)
                    dfs(i+1)
                    board[i][c]="."
                    negdiag.discard(i-c)
                    posdiag.discard(i+c)
                    col.discard(c)
                else:
                    continue
            
        dfs(0)
        return res



        

        