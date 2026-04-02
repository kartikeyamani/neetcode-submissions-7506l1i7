class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size();
        int n=matrix[0].size();
        int selected_row=-1;
        for(int i=0;i<m;i++)
        {
           if(target>=matrix[i][0] && target<=matrix[i][n-1])
           {
            selected_row=i;
           } 
        }
        if(selected_row==-1) return false;
        int i=0;
        int j=n-1;
        while(i<=j)
        {
            int mid=(i+j)/2;
            if(target==matrix[selected_row][mid])
            {
                return true;
            }
            else if(target<matrix[selected_row][mid])
            {
                j=mid-1;
            }
            else{
                i=mid+1;
            }
        }
        return false;
    }
};
