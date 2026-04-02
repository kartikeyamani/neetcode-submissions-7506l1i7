# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float("-inf")
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)

            self.maxsum=max([self.maxsum,left+root.val+right,root.val])
            return max([root.val,left+root.val,right+root.val])
        val=dfs(root)
        self.maxsum=max(self.maxsum,val)
        return self.maxsum

        