class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int>umap1;
        for(int i=0;i<s1.size();i++)
        {
            umap1[s1[i]]++;
        }
        if(s1.size()<=s2.size())
        {
            int windowsize=s1.size();
            int i=0;int j=0;
            unordered_map<char,int> umap2;
            while(j<windowsize)
            {
                umap2[s2[j]]++;
                j++;
            }
            j--;
           
            while(i<s2.size()&&j<s2.size())
            {
                if(umap1==umap2) return true;
                umap2[s2[i]]--;
                if(umap2[s2[i]]==0)
                {
                    umap2.erase(s2[i]);
                }
                i++;
                j++;
                umap2[s2[j]]++;
            }
        }
        return false;
    }
};
