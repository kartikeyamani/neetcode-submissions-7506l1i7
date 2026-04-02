class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(substring):
            return substring==substring[::-1]
        def dfs(idx):
            res=[]
            if idx>=len(s):
                return [[]]
            for i in range(idx,len(s)):
                substring=s[idx:i+1]
                if ispalindrome(substring):
                    newlist=dfs(i+1)
                    for lst in newlist:
                        res.append([substring]+lst)
            return res
        return dfs(0)    
            

        