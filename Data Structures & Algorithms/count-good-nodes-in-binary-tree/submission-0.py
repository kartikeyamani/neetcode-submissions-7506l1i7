# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        maxval=root.val
        return 1+self.check(root.left,maxval)+self.check(root.right,maxval)
    def check(self,root:TreeNode,maxval:int)->int:
        if root==None:
            return 0
        res=0
        if root.val>=maxval:
            res+=1
        maxval=max(maxval,root.val)
        res+=self.check(root.left,maxval)+self.check(root.right,maxval)
        return res



        