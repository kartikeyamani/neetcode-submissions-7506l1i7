class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> umap1;
        for(int i=0;i<s1.size();i++)
        {
            umap1[s1[i]]++;
        }
        for(int i=0;i<s2.size();i++)
        {
            for(int j=i;j<s2.size();j++)
            {
                string sub=s2.substr(i,j-i+1);
                unordered_map<char,int> umap2;
                for(int k=0;k<sub.size();k++)
                {
                    umap2[sub[k]]++;
                }
                if(umap1==umap2)
                {
                    return true;
                }
            }
        }
        return false;
    }
};
