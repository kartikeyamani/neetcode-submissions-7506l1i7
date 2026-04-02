class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.endofword=True


    def search(self, word: str) -> bool:
        def dfs(i,root):
            for j in range(i,len(word)):
                if word[j] !=".":
                    if word[j] not in root.children:
                        return False
                    root=root.children[word[j]]
                else:
                    for child in root.children.values():
                        if dfs(j+1,child):
                            return True
                    return False 
            return root.endofword
        return dfs(0,self.root)   


        
