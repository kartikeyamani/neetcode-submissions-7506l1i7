"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None
        newdict={}
        def dfs(root):
            if root in newdict:
                return newdict[root]
            if root not in newdict:
                newdict[root]=Node(root.val)
            curr=newdict[root]
            for i in root.neighbors:
                curr.neighbors.append(dfs(i))
            return curr
        return dfs(node)


        