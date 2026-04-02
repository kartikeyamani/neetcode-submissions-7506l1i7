class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<int, unordered_map<char,int>> uumap;
        for(int i=0;i<strs.size();i++)
        {
            unordered_map<char, int> umap;
            for(char ch:strs[i])
            {
                umap[ch]++;
            }
            if(!uumap.empty())
            {
                int flag=0;
               for(auto& pair:uumap)
               {
                    if(pair.second==umap)
                    {
                        res[pair.first].push_back(strs[i]);
                        flag=1;
                    }
               }
               if(flag==0)
               {
                    uumap[res.size()]=umap;
                   vector<string> v;
                    v.push_back(strs[i]);
                    res.push_back(v);
               }
              
            }
            else
            {
                uumap[0]=umap;
                vector<string> vec;
                vec.push_back(strs[i]);
                res.push_back(vec);
            }
        }
        return res;
    }
};
