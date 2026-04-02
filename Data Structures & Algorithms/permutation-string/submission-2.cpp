class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> umap1;
        for(int i=0;i<s1.length();i++)
        {
            umap1[s1[i]]++;
        }
        for(int i=0;i<s2.length();i++)
        {
            for(int len=1;len<=s2.length()-i;len++)
            {
                string sub=s2.substr(i,len);
                unordered_map<char,int> umap2;
                for(int k=0;k<sub.size();k++)
                {
                    umap2[sub[k]]++;
                }
                if(umap1==umap2) return true;
            }
        }
        return false;
    }
};
