class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]
        for i in nums:
            if len(minheap)==k:
                if i>minheap[0]:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap,i)
                else:
                    continue
            else:
                heapq.heappush(minheap,i)
        print(minheap)
        return minheap[0]

        
        