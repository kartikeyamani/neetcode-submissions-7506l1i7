class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue=[]
        queue.append((beginWord,1))
        alphabet="abcdefghijklmnopqrstuvwxyz"
        wlist=set(wordList)
        while queue:
            top,level=queue.pop(0)
            for j in range(0,len(beginWord)):
                for i in alphabet:
                    newstring=top[0:j]+i+top[j+1:]
                    if newstring==endWord and newstring in wlist:
                        return level+1
                    if newstring in wlist:
                        queue.append((newstring,level+1))
                        wlist.discard(newstring)
        return 0



        