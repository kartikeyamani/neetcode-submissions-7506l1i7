class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ##creating adjacency list
        from collections import defaultdict
        adjlist=defaultdict(list)
        indegree={c:0 for w in words for c in w}
        ## We must construct the Directed graph from the strings
        for i in range(len(words)-1):
            firstword=words[i]
            secondword=words[i+1]
            flag=0
            for j in range(min(len(firstword),len(secondword))):
                if firstword[j]!=secondword[j]:
                    adjlist[firstword[j]].append(secondword[j])
                    indegree[secondword[j]]+=1
                    flag=1
                    break
            if flag==0 and len(firstword)>len(secondword):
                return ""
        queue=[c for c in indegree if indegree[c]==0]
        res=[]
        while queue:
            node=queue.pop(0)
            for neighbor in adjlist[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
            res.append(node)
        if len(res)!=len(indegree):
            return ""
        return "".join(res)


        
                

            
