"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newdict={}
        if node==None:
            return node
        def func(root):
            if root in newdict:
                return newdict[root]
            newdict[root]=Node(root.val)
            for neighbor in root.neighbors:
                if neighbor not in newdict:
                    newdict[neighbor]=func(neighbor)
                newdict[root].neighbors.append(newdict[neighbor])
            return newdict[root]
        return func(node)
                

        