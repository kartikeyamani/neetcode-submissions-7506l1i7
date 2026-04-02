class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrome(i,j):
            if i>=j:
                return True
            return s[i]==s[j] and ispalindrome(i+1,j-1)
        dp={}
        def func(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i==j:
                dp[(i,j)]=s[i]
                return s[i]
            
            if ispalindrome(i,j):
                dp[(i,j)]=s[i:j+1]
                return s[i:j+1]
            left=func(i,j-1)
            right=func(i+1,j)
            if len(left)>len(right):
                dp[(i,j)]=left
                return left
            dp[(i,j)]=right
            return right
        return func(0,len(s)-1)
