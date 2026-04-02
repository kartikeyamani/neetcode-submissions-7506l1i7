# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(root):
            if root==None:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i=0
        res=data.split(",")
        def dfs():
            if res[self.i]=="N":
                self.i+=1
                return None
            newnode=TreeNode(int(res[self.i]))
            self.i+=1
            newnode.left=dfs()
            newnode.right=dfs()
            return newnode
            
        return dfs()




