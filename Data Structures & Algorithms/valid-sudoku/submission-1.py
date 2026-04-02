class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset=[set() for _ in range(9)]
        colset=[set() for _ in range(9)]
        boxset=[set() for _ in range(9)]

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j]=='.':
                    continue
                boxnum=(i//3)*3 +(j//3)
                if board[i][j] in rowset[i] or board[i][j] in colset[j] or board[i][j] in boxset[boxnum]:
                    return False
                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                boxset[boxnum].add(board[i][j])
        return True

        