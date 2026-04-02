class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        top=-1
        for i in range(0,len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        for i in range(0,k):
            top=heapq.heappop(nums)
        
        return -top