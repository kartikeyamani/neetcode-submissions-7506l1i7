class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            curr=root
            for char in word:
                if char not in curr.children:
                    curr.children[char]=TrieNode()
                curr=curr.children[char]
            curr.endofword=True
        tempword=[]
        res=set()
        def dfs(i,j,root):
            if i<0 or j<0 or i>len(board)-1 or j>len(board[i])-1:
                return
            if board[i][j]=="-1":
                return
            if board[i][j] not in root.children:
                return
            
            curr=root.children[board[i][j]]
            tempword.append(board[i][j])
            if curr.endofword:
                res.add("".join(tempword))
            temp=board[i][j]
            board[i][j]="-1"
            dfs(i+1,j,curr)
            dfs(i,j+1,curr)
            dfs(i-1,j,curr)
            dfs(i,j-1,curr)
            board[i][j]=temp
            tempword.pop(-1)
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                dfs(i,j,root)
        return list(res)




            




        