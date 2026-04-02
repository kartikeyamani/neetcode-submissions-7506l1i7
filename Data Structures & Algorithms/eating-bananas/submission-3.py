class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        n=len(piles)
        res=float("inf")
        while l<=r:
            mid=(l+r)//2
            total=0
            for i in range(n):
                total+=math.ceil(piles[i]/mid)
            if total<=h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res




