class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(sub):
            return sub==sub[::-1]
        def dfs(i):
            if i>=len(s):
                return [[]]
            tempres=[]
            for j in range(i,len(s)):
                if ispalindrome(s[i:j+1]):
                    smallres=dfs(j+1)
                    for k in smallres:
                        tempres.append([s[i:j+1]]+k)       
            return tempres
        return dfs(0)
        