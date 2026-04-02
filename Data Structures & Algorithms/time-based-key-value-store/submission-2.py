class TimeMap:

    def __init__(self):
        self.newdict={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.newdict[key]=self.newdict.get(key,[])
        self.newdict[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        newlist=self.newdict.get(key,[])
        l=0
        r=len(newlist)-1
        ans=""
        while l<=r:
            mid=l+(r-l)//2
            if newlist[mid][1]<=timestamp:
                ans=newlist[mid][0]
                l=mid+1
            else:
                r=mid-1
        return ans

        
