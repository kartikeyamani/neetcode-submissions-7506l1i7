class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[l]<=nums[mid] and nums[mid]>nums[r]:
                l=mid+1
            elif (nums[mid]<nums[l] and nums[mid]<nums[r]) or (nums[mid]<nums[r] and nums[l]<=nums[mid]):
                r=mid
        return nums[l]
        