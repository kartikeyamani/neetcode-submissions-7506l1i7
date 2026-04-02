class Solution {
public:
    int characterReplacement(string s, int k) {
        int maxlen=0;
        for(int i=0;i<s.size();i++)
        {
            for(int j=i;j<s.size();j++)
            {
                string sub=s.substr(i,j-i+1);
                vector<int> v(26,0);
                int maxfreq=0;
                for(int l=0;l<sub.size();l++)
                {
                    v[sub[l]-'A']++;
                    maxfreq=max(maxfreq,v[sub[l]-'A']);
                }
                int replacement_chars=sub.size()-maxfreq;
                if(replacement_chars<=k){
                    maxlen=max(maxlen,j-i+1);
                }
            }
        }
        return maxlen;
    }
};
