# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        maxdepth=1
        return max(self.func(root.left,maxdepth),self.func(root.right,maxdepth))
    
    def func(self,root:Optional[TreeNode],maxdepth: int) -> int:
        if root==None:
            return maxdepth
        return max(self.func(root.left,maxdepth+1),self.func(root.right,maxdepth+1))
        
        


        