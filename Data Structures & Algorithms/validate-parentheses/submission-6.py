class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]
        for i in range(0,len(s)):
            if s[i]=='{' or s[i]=='[' or s[i]=='(':
                temp.append(s[i])
            elif s[i]==']':
                if len(temp)==0 or temp.pop()!='[':
                    return False
            elif s[i]=='}':
                if len(temp)==0 or temp.pop()!='{':
                    return False
            elif s[i]==')':
                if len(temp)==0 or temp.pop()!='(':
                    return False
        if len(temp)==0:
            return True
        return False
                

        