class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #creating an adjacency list
        from collections import defaultdict
        adjlist=defaultdict(list)
        for row in edges:
            adjlist[row[0]].append(row[1])
            adjlist[row[1]].append(row[0])
        visited=[0]*n
        def dfs(i):
            if visited[i]==1:
                return
            visited[i]=1
            for r in adjlist[i]:
                dfs(r)
        final=0
        for i in range(n):
            if visited[i]==0:
                final+=1
                dfs(i)
        return final

            
            
        