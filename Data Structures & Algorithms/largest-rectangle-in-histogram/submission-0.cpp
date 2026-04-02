class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // First what we want to do ?
        // We need to find out the smallest rectangle to the left and right of you.
        stack<int> st;
        vector<int> left(heights.size());
        vector<int> right(heights.size());

        //For calculating the left smallest rectangle
        for(int i=0;i<heights.size();i++)
        {
            while(!st.empty() && heights[st.top()]>=heights[i])
            {
                st.pop();
            }

            left[i]=st.empty()?-1:st.top();

            st.push(i);
        }
        stack<int> new_st;
        //For calculating the smallest element in the right side of index.
        for( int i=heights.size()-1;i>=0;i--)
        {
            while(!new_st.empty() && heights[new_st.top()]>=heights[i])
            {
                new_st.pop();
            }

            right[i]=new_st.empty()?heights.size():new_st.top();

            new_st.push(i);
        }
        //Finding the maximum area
        int maxi=INT_MIN;
        for(int i=0;i<heights.size();i++)
        {
            int width=(right[i])-(left[i]+1);
            int area=width*heights[i];
            maxi=max(maxi,area);
        }
        return maxi;



        
    }
};
