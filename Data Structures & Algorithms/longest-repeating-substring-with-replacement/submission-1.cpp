class Solution {
public:
    int characterReplacement(string s, int k) {
        int left=0;
        int right=0;
        vector<int> v(26,0);
        int maxfreq=0;
        int maxlen=0;
        while(left<s.size()&&right<s.size())
        {
            v[s[right]-'A']++;
            maxfreq=max(maxfreq,v[s[right]-'A']);
            int windowsize=right-left+1;
            int replacement_chars=windowsize-maxfreq;
            if(replacement_chars<=k)
            {
                maxlen=max(maxlen,windowsize);
            }
            else
            {
                v[s[left]-'A']--;
                left++;
            }
             right++;
        }
        return maxlen;
    }
};
