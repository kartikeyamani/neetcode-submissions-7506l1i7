class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=len(nums1)
        b=len(nums2)
        total=a+b
        half=total//2
        A=nums1
        B=nums2
        if len(nums1) > len(nums2):
            A,B=B,A
        l=0
        r=len(A)-1
        mid=(l+r)//2
        while True:
             j=half-mid-2
             Aleft=A[mid] if mid>=0 else float("-infinity")
             Aright=A[mid+1] if mid<len(A)-1 else float("infinity")
             Bleft=B[j] if j>=0 else float("-infinity")
             Bright=B[j+1] if j<len(B)-1 else float("infinity")

             if Aleft<=Bright and Bleft<=Aright:
                # This is true, so this is correct partition
                if total%2:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
             elif Aleft > Bright:
                mid=mid-1
             else:
                mid=mid+1




            
        