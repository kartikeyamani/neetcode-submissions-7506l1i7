class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr=""
        for i in strs:
            newstr+=str(len(i))+"#"+i
        return newstr

    def decode(self, s: str) -> List[str]:
        newlist=[]
        i=0
        while i<len(s):
                j=i
                while s[j] != "#":
                     j+=1
                newnum=int(s[i:j])
                i=j+1
                newlist.append(s[i:i+newnum])
                i=i+newnum
        return newlist

            



