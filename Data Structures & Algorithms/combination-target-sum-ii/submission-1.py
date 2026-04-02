class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        visited=set()
        res=[]
        def dfs(temp,index,target):
            
            if target==0:
                res.append(temp.copy())
                return
            if target<0 or index>=len(candidates):
                return
            temp.append(candidates[index])

            dfs(temp,index+1,target-candidates[index])
            temp.pop()

            while index<len(candidates)-1 and candidates[index]==candidates[index+1]:
                index+=1
            
            dfs(temp,index+1,target)


        candidates.sort()
        dfs([],0,target)
        return res

