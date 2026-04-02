# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return None
        bfs=[root]
        while bfs:
            node=bfs.pop(0)
            node.left,node.right=node.right,node.left
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return root
            
        
        