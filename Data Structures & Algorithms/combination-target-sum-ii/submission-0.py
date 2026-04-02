class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        temp=[]
        def dfs(i,currsum):
            if target==currsum:
                res.append(temp.copy())
                return
            if target<currsum or i>len(candidates)-1:
                return
            temp.append(candidates[i])
            dfs(i+1,currsum+candidates[i])
            temp.pop()
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,currsum)
        dfs(0,0)
        return res

        