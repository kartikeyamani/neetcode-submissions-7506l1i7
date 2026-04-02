class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result;
         for(int i=0;i<temperatures.size()-1;i++)
         {
            int j=i+1;
            int count=0;
            while(j<temperatures.size() && temperatures[i]>=temperatures[j])
            {
                j++;
            }
            if(j>=temperatures.size())
            {
                result.push_back(0);
            }
            else{
                result.push_back(j-i);
            }
         }
         result.push_back(0);
         return result;
    }
};
