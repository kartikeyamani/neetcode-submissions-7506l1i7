# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,root:Optional[TreeNode],subroot:Optional[TreeNode]):
        if not root and not subroot:
            return True
        if (root and not subroot) or (not root and subroot) or (root and subroot and root.val!=subroot.val):
            return False
        return self.helper(root.left,subroot.left) and self.helper(root.right,subroot.right) 
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        

        if root and subRoot and root.val==subRoot.val:
            if self.helper(root,subRoot):
                return True
        
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        

        