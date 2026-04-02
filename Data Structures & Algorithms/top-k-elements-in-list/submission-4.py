class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for i in nums:
            counts[i]=counts.get(i,0)+1
        
        sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        res=[]
        for elem in sorted_list[:k]:
            res.append(elem[0])
        return res

        