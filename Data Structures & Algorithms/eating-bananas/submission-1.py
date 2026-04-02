class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxvalue=0
        for i in piles:
            maxvalue=max(maxvalue,i)
        l=1
        r=maxvalue
        res=maxvalue
        while l<=r:
            mid=(l+(r-l)//2)
            time=0
            for i in piles:
                time+=math.ceil(i/mid)
            if time<=h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res



        