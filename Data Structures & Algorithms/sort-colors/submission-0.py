class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                count0+=1
            elif nums[i]==1:
                count1+=1
            else:
                count2+=1
        for i in range(0,len(nums)):
            if count0>0:
                nums[i]=0
                count0=count0-1
            elif count1>0:
                nums[i]=1
                count1=count1-1
            else:
                nums[i]=2
                count2=count2-1
        