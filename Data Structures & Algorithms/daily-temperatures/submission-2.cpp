class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> st;
        int i=0;
        int j=0;
        vector<int> res(temperatures.size(),0);
        for(int i=0;i<temperatures.size();i++)
        {
            while(!st.empty() && temperatures[st.top()]<temperatures[i])
            {
                int top=st.top();
                st.pop();
                res[top]=i-top;
            }
            st.push(i);
        }
        while(!st.empty())
        {
            res[st.top()]=0;
            st.pop();
        }
        return res;
    }
};
