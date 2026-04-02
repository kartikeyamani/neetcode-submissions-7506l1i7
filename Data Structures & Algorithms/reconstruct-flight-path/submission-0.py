class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        adjlist=defaultdict(list)
        for lst in tickets:
            adjlist[lst[0]].append(lst[1])
        for i in adjlist:
            adjlist[i].sort(reverse=True)
        res=[]
        def dfs(node):
            while adjlist[node]:
                nextdis=adjlist[node].pop()
                dfs(nextdis)
            res.append(node)
        dfs("JFK")
        return res[::-1]



        