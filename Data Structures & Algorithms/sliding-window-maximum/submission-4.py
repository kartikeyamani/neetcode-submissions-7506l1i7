class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        l=0
        r=0
        while r<len(nums):
            if len(q)==0:
                q.append(r)
            elif nums[q[-1]] >= nums[r]:
                q.append(r)
            else:
                while len(q)!=0 and nums[q[-1]]<nums[r]:
                    q.pop()
                q.append(r)
            if r-l+1==k:
                while q[0]<l:
                    q.popleft()
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res
                




        