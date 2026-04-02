# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        trueornot=[0]
        left=self.func(root.left,trueornot)
        right=self.func(root.right,trueornot)
        if trueornot[0]==1:
            return False
        if abs(left-right)>1:
            return False
        return True


    def func(self,root: Optional[TreeNode],trueornot:list) ->int:
        if root==None:
            return 0
        left=self.func(root.left,trueornot)
        right=self.func(root.right,trueornot)
        
        if abs(left-right)>1:
            trueornot[0]=1
        return max(left,right)+1
    
        