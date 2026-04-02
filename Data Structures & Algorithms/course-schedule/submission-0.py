class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ##preparing a adjacency list
        from collections import defaultdict
        adjacencylist=defaultdict(list)
        for row in prerequisites:
            adjacencylist[row[1]].append(row[0])
        visited=[0]*numCourses
        pathvisited=[0]*numCourses
        def dfs(node):
            if pathvisited[node]==1:
                return False
            if visited[node]==1:
                return True
            
            visited[node]=1
            pathvisited[node]=1
            for i in adjacencylist[node]:
                if dfs(i)==False:
                    return False
                # if visited[i]==1 and pathvisited[i]==1:
                #     return False
            pathvisited[node]=0
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return False
        return True

                



            


        

        