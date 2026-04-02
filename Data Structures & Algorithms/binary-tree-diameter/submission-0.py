# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdepth=[0]
        if root==None:
            return maxdepth[0]
        left=self.func(root.left,maxdepth)
        right=self.func(root.right,maxdepth)
        return max(maxdepth[0],left+right)
    def func(self,root: Optional[TreeNode],maxdepth: list) ->int:
        if root==None:
            return 0
        left=self.func(root.left,maxdepth)
        right=self.func(root.right,maxdepth)
        maxdepth[0]=max(maxdepth[0],left+right)
        return max(left,right)+1

        
        
        