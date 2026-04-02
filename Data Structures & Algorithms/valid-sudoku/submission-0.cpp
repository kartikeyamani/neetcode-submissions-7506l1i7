class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, set<char>> rows;
        unordered_map<int, set<char>> cols;
        unordered_map<int, set<char>> boxes;
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++)
            {
                
                if(board[i][j]=='.') continue;
                int box=(i/3)*3+(j/3);

                if(rows[i].count(board[i][j])) return false;
                rows[i].insert(board[i][j]);

                if(cols[j].count(board[i][j]))return false;
                cols[j].insert(board[i][j]);

                if(boxes[box].count(board[i][j])) return false;
                boxes[box].insert(board[i][j]);
            }
        }
        return true;
    }
    
};
