# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root==None:
            return None
        commonans=[root]
        left=self.check(p,q,root.left,commonans)
        right=self.check(p,q,root.right,commonans)
        
        return commonans[0]
    def check(self,p: TreeNode, q: TreeNode,root: TreeNode,commonans:list)-> bool:
        if root==None:
            return False

        left=self.check(p, q,root.left,commonans)
        right=self.check(p,q,root.right,commonans)
        if left and right:
            commonans[0]=root
        if root.val==p.val or root.val==q.val:
            if left or right:
                commonans[0]=root
            return True
        return left or right



        