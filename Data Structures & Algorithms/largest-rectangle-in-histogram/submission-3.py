class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # n=len(heights)
        # right=[n]*n
        # left=[-1]*n
        # st1=[]
        # st2=[]
        # for i in range(n):
        #     if st1:
        #         while st1 and st1[-1][0]>heights[i]:
        #             right[st1[-1][1]]=i
        #             st1.pop()
        #     st1.append((heights[i],i))
        # for i in range(n-1,-1,-1):
        #     if st2:
        #         while st2 and st2[-1][0]>heights[i]:
        #             left[st2[-1][1]]=i
        #             st2.pop()
        #     st2.append((heights[i],i))
        # maxarea=0
        # for i in range(n):
        #     height=heights[i]
        #     width=right[i]-left[i]-1
        #     maxarea=max(maxarea,height*width)
        # return maxarea
        heights.append(0)
        n=len(heights)
        stack=[(-1,-1)]
        maxarea=0
        for i in range(n):
            while stack[-1][0]>heights[i]:
                right=i
                height=stack.pop(-1)[0]
                left=stack[-1][1]
                maxarea=max(maxarea,(right-left-1)*height)  

            stack.append((heights[i],i))
        return maxarea
        

        

        