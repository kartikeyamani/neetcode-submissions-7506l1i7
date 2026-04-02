class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,col,i):
            if i==len(word):
                return True
            if row<0 or row>len(board)-1 or col<0 or col>len(board[0])-1:
                return False
            if board[row][col]!=word[i]:
                return False
            if board[row][col]=="-1":
                return False
            temp=board[row][col]
            board[row][col]="-1"

            res=dfs(row+1,col,i+1) or dfs(row,col+1,i+1) or dfs(row-1,col,i+1) or dfs(row,col-1,i+1)

            board[row][col]=temp
            return res

        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if dfs(row,col,0):
                    return True
        return False
        
            
        