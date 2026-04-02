class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        maxlen=0
        n=len(s)
        alpha=[0]*26
        while l<n and r<n and l<=r:
            alpha[ord(s[r])-ord('A')]+=1
            maxi=0
            for i in range(26):
                maxi=max(maxi,alpha[i])
            length=r-l+1
            if r==n-1:
                print(l)
                print(alpha)
                print(maxi)
            if length-maxi>k:
                #print(r)
                while l<=r and length-maxi>k:
                    alpha[ord(s[l])-ord('A')]-=1
                    l+=1
                    maxi=0
                    for i in range(26):
                        maxi=max(maxi,alpha[i])
                    length=r-l+1
            else:
                maxlen=max(maxlen,length)
            r+=1
        return maxlen


        