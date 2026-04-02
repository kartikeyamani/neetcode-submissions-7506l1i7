class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.nums.sort()

        

    def add(self, val: int) -> int:
        i=0
        while i<len(self.nums) and self.nums[i]<val :
            i+=1
        self.nums.insert(i,val)

        return self.nums[len(self.nums)-self.k]
        

        
