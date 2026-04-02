class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=list(range(len(edges)+1))
        rank=[0]*(len(edges)+1)
        def find(X):
            if parent[X]!=X:
                parent[X]=find(parent[X])
            return parent[X]
        def union(X,Y):
            rootx=find(X)
            rooty=find(Y)
            if rootx!=rooty:
                if rank[rootx]>rank[rooty]:
                    parent[rooty]=rootx
                elif rank[rootx]<rank[rooty]:
                    parent[rootx]=rooty
                else:
                    rank[rootx]+=1
                    parent[rooty]=rootx
                return True
            return False
        for lst in edges:
            if union(lst[0],lst[1])==False:
                return lst
            
        
        