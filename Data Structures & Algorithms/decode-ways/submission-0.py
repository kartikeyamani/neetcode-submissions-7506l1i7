class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        def func(ind):
            if ind==n:
                return 1
            if ind==n-1 and s[ind]!='0':
                return 1
            if s[ind]=='0':
                return 0
            pickone=func(ind+1)
            picktwo=0
            if 10<=int(s[ind:ind+2])<=26:
                picktwo=func(ind+2)
            return pickone+picktwo
        return func(0)


        