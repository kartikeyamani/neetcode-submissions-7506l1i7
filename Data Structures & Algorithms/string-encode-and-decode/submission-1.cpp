class Solution {
public:

    string encode(vector<string>& strs) {
         string new_str;
        for(int i=0;i<strs.size();i++)
        {
            int length=strs[i].size();
           new_str+=to_string(length)+'#'+strs[i];
        }
        //cout<<new_str;
        return new_str;
    }

    vector<string> decode(string s) {
        int len=s.size();
        int i=0;
        vector<string> v;
        while(i<len)
        {
            string str="";
            while(s[i]!='#')
            {
                str+=s[i];
                i++;
            }
            int num=stoi(str);
            v.push_back(s.substr(i+1,num));
            i=i+1+num;
        }
        
        return v;
    }
};
