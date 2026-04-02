class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profit=0
        while l<len(prices) and r<len(prices):
            if prices[l]<prices[r]:
                val=prices[r]-prices[l]
                profit=max(profit,val)
            else:
                l=r
            r+=1
        return profit

        