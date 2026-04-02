# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.newstr=[]
        def dfs(root):
            if not root:
                self.newstr+='N'
                return
            self.newstr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(self.newstr)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #print(data)
        self.idx=0
        lst=data.split(",")
        def dfs():
            if self.idx>=len(lst):
                return
            if lst[self.idx]!='N':
                root=TreeNode(int(lst[self.idx]))
                self.idx+=1
                root.left=dfs()
                root.right=dfs()
                return root
            else:
                self.idx+=1
                return None
        return dfs()
            
            




