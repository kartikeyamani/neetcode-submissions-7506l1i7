class Solution {
public:
    int maxArea(vector<int>& heights) {
        int i=0;
        int j=heights.size()-1;
        int maxi=0;
        while(i<j)
        {
            maxi=max(maxi,(j-i)*min(heights[i],heights[j]));
            if(heights[i]<=heights[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return maxi;
    }
};
