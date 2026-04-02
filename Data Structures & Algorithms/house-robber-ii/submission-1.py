class Solution:
    def rob(self, nums: List[int]) -> int:
        ## Very similar to HR 1, but here if we take first element we avoid last
        ## If we take last element we avoid first.
        if len(nums)==1:
            return nums[0]
            
        def func(newvec):
            n=len(newvec)
            dp=[0]*(n)
            dp[n-1]=newvec[n-1]
            for i in range(n-2,-1,-1):
                pick=newvec[i]
                if i!=n-2:
                    pick+=dp[i+2]
                notpick=0+dp[i+1]
                dp[i]=max(pick,notpick)
            return dp[0]
        newvec=[]
        for i in range(len(nums)-1):
            newvec.append(nums[i])
        max1=func(newvec)
        newvec1=[]
        for i in range(1,len(nums)):
            newvec1.append(nums[i])
        max2=func(newvec1)
        return max(max1,max2)



        
        
            
        