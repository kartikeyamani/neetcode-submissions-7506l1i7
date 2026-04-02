# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(root):
            if not root:
                return (0,True)
            left=helper(root.left)
            right=helper(root.right)

            if left[1] and right[1] and abs(right[0]-left[0])<=1:
                return (1+max(left[0],right[0]),True)
            
            return (-1,False)
         
        res=helper(root)
        return res[1]
        
        