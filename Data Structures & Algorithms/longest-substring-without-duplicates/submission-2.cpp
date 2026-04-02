class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxlen=0;
        for(int i=0;i<s.size();i++)
        {
            for(int j=i;j<s.size();j++)
            {
                string sub=s.substr(i,j-i+1);
                if(checkduplicates(sub))
                {
                    break;
                }
                else
                {
                    maxlen=max(maxlen,j-i+1);
                }
            }
        }
        return maxlen;
    }
    bool checkduplicates(string sub)
    {
        unordered_set<char> uset;
        for(char ch:sub)
        {
            if(uset.count(ch)) return true;
            uset.insert(ch);
        }
        return false;
    }
};
