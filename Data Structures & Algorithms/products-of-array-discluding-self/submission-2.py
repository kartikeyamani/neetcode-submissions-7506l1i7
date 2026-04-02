class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        st=[]
        rev=[]
        res=[]
        n=len(nums)
        for i in range(len(nums)):
            if i==0:
                st.append(nums[i])
            else:
                st.append(st[-1]*nums[i])
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                rev.append(nums[i])
            else:
                rev.append(rev[-1]*nums[i])
        for i in range(n):
            if i==0:
                res.append(rev[n-i-2])
            elif i==n-1:
                res.append(st[i-1])
            else:
                val=rev[n-i-2]*st[i-1]
                res.append(val)
        return res
        

        