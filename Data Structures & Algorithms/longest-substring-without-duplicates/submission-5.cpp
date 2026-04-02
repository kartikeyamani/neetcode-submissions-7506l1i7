class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxlen=0;
        unordered_map<char,int> umap;
        int i=0;int j=0;
        while(i<s.size() && j<s.size())
        {
            if(umap.count(s[j]) && umap[s[j]]>=i)
            {
                i=umap[s[j]]+1;
                umap[s[j]]=j;
                maxlen=max(maxlen,j-i+1);
                j++;
            }
            else
            {
                umap[s[j]]=j;
                maxlen=max(maxlen,j-i+1);
                j++;
            }
        }
        return maxlen;
    }
};
