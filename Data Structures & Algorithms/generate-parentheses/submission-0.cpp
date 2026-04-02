class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string curr;
        curr.reserve(2*n);
        func(ans,curr,n,0,0);
        return ans;
    }
    void func(vector<string> &ans,string &curr,int n, int open,int close)
    {
       if(close>open)
         return;
       if(close==open && open ==n)
       {
         ans.push_back(curr);
         return;
       }
       if(open<n)
       {
          curr.push_back('(');
          func(ans,curr,n,open+1,close);
          curr.pop_back();
       }
       if(close<open)
       {
          curr.push_back(')');
          func(ans,curr,n,open,close+1);
          curr.pop_back();
       }     
       return;
    }
};
