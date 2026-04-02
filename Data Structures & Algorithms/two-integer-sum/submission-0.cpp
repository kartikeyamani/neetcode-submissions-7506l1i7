class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> umap;
        vector<int> res;
        for(int i=0;i<nums.size();i++)
        {
            int dummy=target-nums[i];
            if(umap.find(dummy)!=umap.end())
            {
                res.push_back(umap[dummy]);
                res.push_back(i);
                return res;
            }
            else
            {
                umap[nums[i]]=i;
            }
        }
        return res;
    }
};
