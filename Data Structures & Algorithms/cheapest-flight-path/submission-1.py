class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        queue=[[0,src,0]]
        from collections import defaultdict
        adjlist=defaultdict(list)
        ## creating an adjacency list
        for lst in flights:
            adjlist[lst[0]].append((lst[1],lst[2]))
        res=float("inf")
        while queue:
            stops,node,weight=queue.pop(0)
            if stops<=k+1 and node==dst:
                res=min(res,weight)
                continue
            if stops==k+1:
                continue
            for lst in adjlist[node]:
                queue.append([stops+1,lst[0],weight+lst[1]])
        if res==float("inf"):
            return -1
        return res
            
            


        