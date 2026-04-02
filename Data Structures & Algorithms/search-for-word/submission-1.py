class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag=[False]
        temp=[]
        def dfs(i,j):
            if "".join(temp)==word:
                flag[0]=True
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1:
                return
            if board[i][j]=="-1":
                return
            temp.append(board[i][j])
            temporary=board[i][j]
            board[i][j]="-1"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            board[i][j]=temporary
            temp.pop()

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                dfs(i,j)

        return flag[0]


        
        