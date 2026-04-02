class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> umap;
        for(char c:s)
        {
            umap[c]++;
        }
        for(char c:t)
        {
            if(umap.find(c)==umap.end()||umap[c]==0)
                return false;
            else{
                umap[c]--;
            }
        }
        for(auto& pair:umap)
        {
            if(pair.second!=0)
                return false;
        }
        return true;
    }
};
