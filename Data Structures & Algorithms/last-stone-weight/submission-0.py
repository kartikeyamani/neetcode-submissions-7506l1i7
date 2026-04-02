class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0,len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1=heapq.heappop(stones)
            stone2=heapq.heappop(stones)

            ans=stone1-stone2
            heapq.heappush(stones,ans)
        if len(stones)==1:
            return -heapq.heappop(stones)

        
        
