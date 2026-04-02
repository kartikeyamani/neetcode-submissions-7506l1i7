# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        queue=[root,"$"]
        ans=[]
        while queue:
            temp=[]
            while queue[0]!="$":
                node=queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
            queue.pop(0)
            if queue:
                queue.append("$")
        final=[]
        for i in ans:
            final.append(i[-1])
        return final
                


        