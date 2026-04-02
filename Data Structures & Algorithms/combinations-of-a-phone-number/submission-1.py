class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        newdict={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        def dfs(i):
            if i==len(digits)-1:
                return list(newdict[int(digits[i])])
            newlist=dfs(i+1)
            templist=list(newdict[int(digits[i])])
            res=[]
            for i in range(len(newlist)):
                for j in range(len(templist)):
                    res.append(templist[j]+newlist[i])
            return res
        return dfs(0)
            


        