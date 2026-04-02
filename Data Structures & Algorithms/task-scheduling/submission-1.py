class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        newdict={}
        for i in range(len(tasks)):
            val=newdict.get(tasks[i],0)
            newdict[tasks[i]]=val+1
        maxheap=[]
        for key,val in newdict.items():
            heapq.heappush(maxheap,-val)
        time=0
        queue=[]
        while True:
            while queue and queue[0][1]<=time:
                heapq.heappush(maxheap,queue[0][0])
                queue.pop(0)
            if not queue and not maxheap:
                break
            if  not maxheap:
                time+=1
                continue
            
            top=heapq.heappop(maxheap)
            time+=1
            freq=top+1
            if freq==0:
                continue
            
            nextavailable=time+n
            #print(nextavailable)
            queue.append((freq,nextavailable))
        return time


        