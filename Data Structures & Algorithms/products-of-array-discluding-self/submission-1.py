class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftmulti=[]
        rightmulti=[]
        for i in nums:
            if not leftmulti:
                leftmulti.append(i)
            else:
                num=leftmulti[-1]*i
                leftmulti.append(num)
        for i in range(len(nums)-1,-1,-1):
            if not rightmulti:
                rightmulti.append(nums[i])
            else:
                num=rightmulti[-1]*nums[i]
                rightmulti.append(num)
        rightmulti.reverse()
        ans=[]
        for i in range(0,len(nums)):
            result=1
            if len(nums)>1:
                if i==0:
                    result=result*rightmulti[i+1]
                elif i==len(nums)-1:
                    result=result*leftmulti[i-1]
                else:
                    result=leftmulti[i-1]*rightmulti[i+1]
            ans.append(result)
        return ans
                    



            

        

        