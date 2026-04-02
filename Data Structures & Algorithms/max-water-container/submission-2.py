class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxwater=float("-inf")
        while l<r:
            value=min(heights[l],heights[r])
            dist=r-l
            maxwater=max(maxwater,value*dist)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxwater

        