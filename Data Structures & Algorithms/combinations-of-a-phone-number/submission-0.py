class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        newdict={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        def dfs(i):
            if i==len(digits)-1:
                return newdict[int(digits[i])]
            newlist=dfs(i+1)
            currlist=newdict[int(digits[i])]
            tempres=[]
            for k in range(0,len(currlist)):
                for j in range(0,len(newlist)):
                    tempres.append(currlist[k]+newlist[j])
            return tempres
        return dfs(0)

            

        