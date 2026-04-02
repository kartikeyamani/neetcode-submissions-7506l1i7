class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ##create adjacency list
        from collections import defaultdict
        adjlist=defaultdict(list)
        for row in edges:
            adjlist[row[0]].append(row[1])
            adjlist[row[1]].append(row[0])
        visited=[0]*n
        def bfs(i):
            if visited[i]==1:
                return True
            queue=[]
            queue.append((i,-1))
            while queue:
                element,parent=queue.pop(0)
                visited[element]=1
                for x in adjlist[element]:
                    if visited[x]==1 and x!=parent:
                        return False
                    if visited[x]!=1:
                        visited[x]=1
                        queue.append((x,element))
                    
            return True
        if bfs(0)==False:
            return False
        for t in visited:
            if t==0:
                return False
        return True
                


            


        