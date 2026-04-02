class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums=[]
        heapq.heapify(nums)
        for i in stones:
            heapq.heappush(nums,-i)
        while len(nums)>1:
            val1=heapq.heappop(nums)
            val2=heapq.heappop(nums)

            if val1-val2 !=0:
                heapq.heappush(nums,val1-val2)
        if not nums:
            return 0
        return -nums[0]






        