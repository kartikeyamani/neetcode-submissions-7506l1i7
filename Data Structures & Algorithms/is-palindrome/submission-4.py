class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<=j:
            while i<j and s[j].lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                j-=1
            while i<j and s[i].lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                i+=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
        