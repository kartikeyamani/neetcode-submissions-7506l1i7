class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        

    def addNum(self, num: int) -> None:
            
        if not self.minheap:
            heapq.heappush(self.minheap,num)
        elif num>self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap,-num)
        while abs(len(self.minheap)-len(self.maxheap)) >1:
            if len(self.minheap)>len(self.maxheap):
                top=heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,-top)
            else:
                top=heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,-top)

    def findMedian(self) -> float:
        if self.minheap or self.maxheap:
            if len(self.minheap)==len(self.maxheap):
                top1=self.minheap[0]
                top2=-self.maxheap[0]
                return (top1+top2)/2.0
            elif len(self.minheap)>len(self.maxheap):
                return self.minheap[0]
            
        return -self.maxheap[0]


        
        