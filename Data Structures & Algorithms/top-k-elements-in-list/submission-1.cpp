class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> umap;
        for(int i=0;i<nums.size();i++)
        {
            if(umap.find(nums[i])!=umap.end())
            {
                umap[nums[i]]++;
            }
            else
            {
                umap[nums[i]]=1;
            }
        }
        
        vector<pair<int, int>> vec(umap.begin(), umap.end());
        sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;
    });
    vector<int> v;
    int dummy=k;
     for (const auto& p : vec) 
    {
        if(dummy)
        {
            v.push_back(p.first);
            dummy--;
        }
    }
     return v;
    }
};
