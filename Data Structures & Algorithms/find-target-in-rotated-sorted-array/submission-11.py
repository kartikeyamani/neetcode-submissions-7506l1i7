class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        
        l,r=0,n-1
        if n==1 and target==nums[0]:
            return 0
        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                return mid
            if nums[mid]>nums[r]:
                if target<nums[l] or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target>nums[r] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1

        