class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        temp=[]
        def dfs(openN,closedN):
            if openN==closedN==n:
                res.append("".join(temp))
                return
            if openN<n:
                temp.append("(")
                dfs(openN+1,closedN)
                temp.pop()
            if closedN<openN:
                temp.append(")")
                dfs(openN,closedN+1)
                temp.pop()
        dfs(0,0)
        return res
            


        