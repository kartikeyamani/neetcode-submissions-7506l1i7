class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        adjlist=defaultdict(list)
        for row in prerequisites:
            adjlist[row[1]].append(row[0])
        stack=[]
        visited=[0]*numCourses
        pathvisited=[0]*numCourses
        def dfs(i):
            if pathvisited[i]==1:
                return False
            if visited[i]==1:
                return True
            visited[i]=1
            pathvisited[i]=1
            for x in adjlist[i]:
                if dfs(x)==False:
                    return False
            pathvisited[i]=0
            stack.append(i)
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return stack[::-1]

            


        
        
        
        for i in range(numCourses):
            if visited[i]==0:
                dfs(i)
        

        