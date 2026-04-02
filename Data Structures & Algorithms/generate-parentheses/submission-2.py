class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(close,op,temp):
            if close==op==n:
                res.append("".join(temp))
                return
            if op<n:
                temp.append('(')
                dfs(close,op+1,temp)
                temp.pop()
            if close<op:
                temp.append(')')
                dfs(close+1,op,temp)
                temp.pop()
        dfs(0,0,[])
        return res
