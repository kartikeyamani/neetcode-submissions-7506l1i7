class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count=defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]]=1+count.get(nums[i],0)
        freq=[[] for _ in range(len(nums)+1)]
        for key,val in count.items():
            freq[val].append(key)
        for i in range(len(freq)-1,-1,-1):
            if len(freq[i])!=0:
                for num in freq[i]:
                    if len(res)<k:
                        res.append(num)
                    else:
                        return res
        return res
        

                    



            

        