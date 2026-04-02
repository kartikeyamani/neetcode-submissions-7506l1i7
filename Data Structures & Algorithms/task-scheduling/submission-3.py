class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxheap=[-count for count in freq.values()]
        heapq.heapify(maxheap)

        q=deque()
        time=0
        while maxheap or q:
            time+=1

            if maxheap:
                val=heapq.heappop(maxheap)
                if val!=-1:
                    q.append((val+1,time+n))
            if q and q[0][1]<=time:
                res=q.popleft()
                heapq.heappush(maxheap,res[0])
                
        return time





        