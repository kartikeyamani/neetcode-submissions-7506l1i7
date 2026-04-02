class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        c=len(board[0])
        r=len(board)
        def dfs(i,j,idx,visited):
            if (i,j) in visited:
                return False
            if idx>=len(word):
                return True
            if i>=r or j>=c or i<0 or j<0 or board[i][j]!=word[idx]:
                return False
            visited.add((i,j))
            res= dfs(i+1,j,idx+1,visited) or dfs(i,j-1,idx+1,visited) or dfs(i,j+1,idx+1,visited) or dfs(i-1,j,idx+1,visited)
            visited.remove((i,j))
            return res

        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    visited=set()
                    if dfs(i,j,0,visited):
                        return True
        return False

        