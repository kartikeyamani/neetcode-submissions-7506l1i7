class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False]*len(s) for _ in range(len(s))]
        res=0
        for i in range(n-1,-1,-1):
            for j in range(i,len(s)):
                if i==j:
                    dp[i][j]=True
                    res+=1
                elif j-i<2 and s[i]==s[j]:
                    dp[i][j]=True
                    res+=1
                elif s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    res+=1
        return res

                
                    
        