# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue=[root]
        while queue:
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val==subRoot.val and self.func(node,subRoot):
                return True
        return False
    def func(self,root: Optional[TreeNode],subRoot: Optional[TreeNode])->bool :
        if root==None and subRoot==None:
            return True
        if root and subRoot and root.val==subRoot.val:
            return self.func(root.left,subRoot.left) and self.func(root.right,subRoot.right)
        else:
            return False
                
        
            


        