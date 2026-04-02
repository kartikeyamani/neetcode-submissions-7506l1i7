class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo={}

        def ispalindrome(i,j):
            if i>=j:
                return True
            return s[i]==s[j] and ispalindrome(i+1,j-1)
        def func(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==j:
                return s[i]
            if ispalindrome(i,j):
                return s[i:j+1]
            str1=func(i+1,j) 
            str2=func(i,j-1)
            if len(str1)>len(str2):
                memo[(i,j)]=str1
                return str1
            memo[(i,j)]=str2
            return str2
        return func(0,len(s)-1)
        

        