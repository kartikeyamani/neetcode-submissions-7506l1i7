class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_dict=dict()
        for char in s:
            if char in new_dict:
                new_dict[char]=new_dict[char]+1
            else:
                new_dict[char]=1
        for char in t:
            if char not in new_dict:
                return False
            elif new_dict[char]==0:
                return False
            else:
                new_dict[char]=new_dict[char]-1
        for key in new_dict.keys():
            if new_dict[key]!=0:
                return False
        return True

        