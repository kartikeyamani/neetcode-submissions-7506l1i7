class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        for i in range(0,len(height)):
            if i==0:
                left.append(height[i])
            else:
                val=max(left[-1],height[i])
                left.append(val)
        right=[]
        for i in range(len(height)-1,-1,-1):
            if i==len(height)-1:
                right.append(height[i])
            else:
                val=max(height[i],right[-1])
                right.append(val)
        right.reverse()
        i=1
        totalwater=0
        for i in range(1,len(height)-1):
            val=min(left[i-1],right[i+1])-height[i]
            if val>0:
                totalwater+=val
        return totalwater


        