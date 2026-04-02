class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        mintill=float("inf")
        for i in range(len(prices)):
            mintill=min(mintill,prices[i])
            maxp=max(maxp,prices[i]-mintill)
        return maxp
        