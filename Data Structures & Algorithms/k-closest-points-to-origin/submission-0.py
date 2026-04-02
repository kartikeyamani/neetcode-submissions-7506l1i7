class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        final=[]
        newdict={}
        for i in points:
            distance=math.sqrt((i[0])**2 + (i[1])**2)
            newtuple=(i[0],i[1])
            newdict[newtuple]=distance
        for key,value in newdict.items():
            heapq.heappush(res,(value,key))
        for _ in range(0,k):
            value,key=heapq.heappop(res)
            #print(top)
            final.append(key)
        return final



        