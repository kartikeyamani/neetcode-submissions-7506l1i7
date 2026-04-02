class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        int flag=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='{'||s[i]=='['||s[i]=='(')
            {
                flag=1;
                st.push(s[i]);
            }
            else if(s[i]=='}')
            {
                if(!st.empty() && st.top()=='{')
                  st.pop();
                else
                  return false;
            }
            else if(s[i]==']')
            {
                 if(!st.empty() && st.top()=='[')
                  st.pop();
                else
                  return false;
            }
            else if(s[i]==')')
            {
                 if(!st.empty() && st.top()=='(')
                  st.pop();
                else
                  return false;
            }
        }

    if(st.empty() && flag==1) return true;
    
    return false;}
};
