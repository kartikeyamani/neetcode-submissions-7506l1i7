# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        newdict={val:idx for idx,val in enumerate(inorder)}
        self.rootidx=0
        def dfs(l,r)->Optional[TreeNode]:
            if l>r:
                return None
            root=TreeNode(val=preorder[self.rootidx])
            newidx=newdict[preorder[self.rootidx]]
            self.rootidx+=1
            root.left=dfs(l,newidx-1)
            root.right=dfs(newidx+1,r)

            return root
        return dfs(0,len(inorder)-1)



            

        