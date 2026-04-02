class Solution {
public:
    string minWindow(string s, string t) {
        int i=0;
        int j=0;
        unordered_map<char,int> umap1;
        int min_len=INT_MAX;
        for(int k=0;k<t.size();k++)
        {
            umap1[t[k]]++;
        }
        int required=umap1.size();
        int formed=0;
        string res="";
        unordered_map<char,int> umap;
        while(j<s.length())
        {
           umap[s[j]]++;
           //check whether this current umap has all the characters present in 
           //string t.
           if(umap1.count(s[j]) && umap[s[j]]==umap1[s[j]])
            formed++;
           
           while(formed==required)
           {
             //update the minimum length
             if(j-i+1<min_len)
             {
                res=s.substr(i,j-i+1);
                min_len=j-i+1;
             }
             umap[s[i]]--;
             if(umap1.count(s[i])&&umap[s[i]]<umap1[s[i]])
              formed--;
            
            i++;
           }
           j++; 
        }
    return res;}
};
