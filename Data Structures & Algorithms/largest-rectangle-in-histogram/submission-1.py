class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rightsmaller=[len(heights)]*len(heights)
        stack=[]
        for i in range(0,len(heights),1):
            while stack and heights[i]<heights[stack[-1]]:
                newindex=stack.pop()
                rightsmaller[newindex]=i
            stack.append(i)
        leftsmaller=[-1]*len(heights)
        newstack=[]
        for i in range(len(heights)-1,-1,-1):
            while newstack and heights[i]<heights[newstack[-1]]:
                newindex=newstack.pop()
                leftsmaller[newindex]=i
            newstack.append(i)
        maxarea=0
        for i in range(0,len(heights)):
            width=rightsmaller[i]-leftsmaller[i]-1
            area=heights[i]*width
            maxarea=max(maxarea,area)
        return maxarea

        
        








        