class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            newdict={}
            for ch in s:
                newdict[ch]= newdict.get(ch,0)+1
            key=tuple(sorted(newdict.items()))
            res[key].append(s)
        return list(res.values())        
                    
                


        