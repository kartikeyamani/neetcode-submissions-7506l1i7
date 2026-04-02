class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        unordered_set<int> karth;
        for(int i=0;i<nums.size();i++)
        {
            karth.insert(nums[i]);
        }
        vector<int> headers;
        int res=1;
        for(int i=0;i<nums.size();i++)
        {
            if(karth.find(nums[i]-1)==karth.end())
            {
                headers.push_back(nums[i]);
            }
        }
        for(int i=0;i<headers.size();i++)
        {
            int num=headers[i];
            int count=1;
            while(karth.find(num+1)!=karth.end())
            {
                count++;
                num++;
                res=max(res,count);
            }
            
        }
        return res;
    }
};
