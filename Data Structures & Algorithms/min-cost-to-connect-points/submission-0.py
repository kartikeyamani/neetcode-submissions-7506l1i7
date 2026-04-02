class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        hp=[]
        res=0
        pointstonodes={(points[i][0],points[i][1]):i for i in range(len(points))}
        parent={i:i for i in range(len(points))}
        rank={i:0 for i in range(len(points))}
        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx!=rooty:
                if rank[rootx]>rank[rooty]:
                    parent[rooty]=rootx
                elif rank[rooty]>rank[rootx]:
                    parent[rootx]=rooty
                else:
                    rank[rootx]+=1
                    parent[rooty]=rootx
                return True
            return False
        ## first we have to find out distances from all points to all other points
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                distance=abs(points[i][0]-points[j][0])+ abs(points[i][1]-points[j][1])
                heapq.heappush(hp,[distance,points[i][0],points[i][1],points[j][0],points[j][1]])
        while hp:
            dis,x1,y1,x2,y2=heapq.heappop(hp)
            x=pointstonodes[(x1,y1)]
            y=pointstonodes[(x2,y2)]
            if union(x,y)==True:
                res+=dis
        return res





        
        