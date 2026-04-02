# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        
        left=self.check(root.left,[float("-inf"),root.val])
        right=self.check(root.right,[root.val,float("inf")])

        if left and right:
            return True
        return False
    def check(self,root: Optional[TreeNode],boundaries:list)->bool:
        if root==None:
            return True
        tempright=boundaries[1]
        templeft=boundaries[0]
        boundaries[1]=root.val
        left=self.check(root.left,boundaries)
        boundaries[0]=root.val
        boundaries[1]=tempright
        right=self.check(root.right,boundaries)

        if left and right:
            if root.val>templeft and root.val< tempright:
                return True
        return False
        