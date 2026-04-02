class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispalindrome(i,j):
            if i>j:
                return True
            return s[i]==s[j] and ispalindrome(i+1,j-1)
        i=0
        j=len(s)-1
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if ispalindrome(i,j):
                    count+=1
        return count
            

        