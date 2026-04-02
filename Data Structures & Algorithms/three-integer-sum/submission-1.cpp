class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
         sort(nums.begin(),nums.end());
         vector<vector<int>> result;
         for(int i=0;i<nums.size();i++)
         {
            int j=i+1;
            int k=nums.size()-1;
            if(i>0 && nums[i]==nums[i-1]) continue;
            while(j<k)
            {
                if(nums[j]+nums[k]== -(nums[i]))
                {
                    vector<int> v;
                    v.push_back(nums[i]);
                    v.push_back(nums[j]);
                    v.push_back(nums[k]);

                    result.push_back(v);
                    while(j<k && nums[j]==nums[j+1]) j++;
                    while(j<k && nums[k]==nums[k-1]) k--;

                    j++;
                    k--;

                }
                else if(nums[j]+nums[k]<(-nums[i]))
                {
                    j++;
                }
                else
                {
                    k--;
                }

            }
         }
         return result;
    }
};
