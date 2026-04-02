class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set=set()
        for i in nums:
            new_set.add(i)

        print(len(new_set))
        print(len(nums))
        if len(new_set)==len(nums):
            return False
        return True
        