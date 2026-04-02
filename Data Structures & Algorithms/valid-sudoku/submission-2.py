class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset=[set() for _ in range(9)]
        colset=[set() for _ in range(9)]
        boxset=[set() for _ in range(9)]

        rows=len(board)
        cols=len(board[0])
        
        for i in range(0,rows):
            for j in  range(0,cols):
                if board[i][j]=='.':
                    continue
                box=(i//3)*3 +(j//3)
                if board[i][j] in rowset[i] or board[i][j] in colset[j] or board[i][j] in boxset[box]:
                    return False
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                boxset[box].add(board[i][j])

        return True
                
        