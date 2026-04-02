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
            curr=root
            for j in range(i,len(word)):
                if word[j]!=".":
                    if word[j] not in curr.children:
                        return False
                    curr=curr.children[word[j]]
                else:
                    for child in curr.children.values():
                        if dfs(j+1,child):
                            return True
                    return False
            return curr.endofword
        return dfs(0,self.root)



        
