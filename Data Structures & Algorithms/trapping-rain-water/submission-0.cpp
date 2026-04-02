class Solution {
public:
    int trap(vector<int>& height) {
        vector<int> left;
        vector<int> right;
        int ans=0;
        for(int i=0;i<height.size();i++)
        {
            if(i==0) left.push_back(height[0]);
            else{
                int res=max(left[i-1],height[i]);
                left.push_back(res);
            }
        }
        for(int i=height.size()-1;i>=0;i--)
        {
            if(i==(height.size()-1)) right.push_back(height[height.size()-1]);
            else{
                int right_last=right[right.size()-1];
                int highest=max(height[i],right_last);
                right.push_back(highest);
            }
        }
        reverse(right.begin(),right.end());
        // for(int i=0;i<right.size();i++)
        // {
        //     cout<<right[i];
        // }
        for(int i=0;i<height.size();i++)
        {
            int res=min(left[i],right[i]);
            if(res>height[i])
            {
                res=res-height[i];
                ans+=res;
            }
        }
        return ans;
    }
};
