class MinStack {
public:
    stack<int> st;
    stack<int> new_st;
    MinStack() {
        
    }
    
    void push(int val) {
        st.push(val);
        int new_min=INT_MAX;
        if(new_st.empty())
        {
            new_min=val;
        }
        else{
            new_min=min(val,new_st.top());
        }
        new_st.push(new_min);
    }
    
    void pop() {
        st.pop();
        new_st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return new_st.top();
    }
};
