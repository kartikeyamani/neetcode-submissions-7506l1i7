class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left;
        for(int i=0;i<nums.size();i++)
        {
            if(i==0)
            {
                left.push_back(1);
                continue;
            }
            int res=left[i-1]*nums[i-1];
            left.push_back(res);
        }
        
        vector<int> right;
        for(int i=nums.size()-1;i>=0;i--)
        {
            if(i==nums.size()-1)
            {
                right.push_back(1);
                continue;
            }
            int res=nums[i+1]*right[right.size()-1];
            right.push_back(res);
        }
        reverse(right.begin(),right.end());
        // for(int i=0;i<right.size();i++)
        // {
        //     cout<<right[i];
        // }
        vector<int> res;
        for(int i=0;i<nums.size();i++)
        {
            res.push_back(left[i]*right[i]);
        }
        return res;

    }
};
