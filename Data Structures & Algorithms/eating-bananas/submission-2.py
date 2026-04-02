class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r 
        while l <= r:
            mid = (l + r) // 2
            numhours = 0
            for p in piles:
                # numhours += (p + mid - 1) // mid
                numhours+=(p//mid)
                if p%mid!=0:
                    numhours+=1
            if numhours <= h:
                res = mid      
                r = mid - 1
            else:
                l = mid + 1   
                
        return res