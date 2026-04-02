class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        from collections import defaultdict
        adjlist=defaultdict(list)
        #creating the adjacency list
        for lst in times:
            adjlist[lst[0]].append((lst[1],lst[2]))
        distance=[float("inf")]*(n+1)
        distance[k]=0
        hp=[(0,k)]
        while hp:
            dis,node=heapq.heappop(hp)
            for neigh,weight in adjlist[node]:
                if distance[neigh]>distance[node]+weight:
                    distance[neigh]=distance[node]+weight
                    heapq.heappush(hp,(distance[neigh],neigh))
        res=-1
        for i in range(1,len(distance)):
            if distance[i]==float("inf"):
                return -1
            else:
                res=max(res,distance[i])
        return res





        


        
        