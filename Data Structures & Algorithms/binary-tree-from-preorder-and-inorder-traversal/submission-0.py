# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.rootidx=0
        newdict={val:idx for idx,val in enumerate(inorder)}
        def check(l,r):
            if l>r:
                return None
            rootval=preorder[self.rootidx]
            self.rootidx +=1
            inorderidx=newdict[rootval]
            root=TreeNode(rootval)
            root.left=check(l,inorderidx-1)
            root.right=check(inorderidx+1,r)

            return root
        return check(0,len(inorder)-1)








        