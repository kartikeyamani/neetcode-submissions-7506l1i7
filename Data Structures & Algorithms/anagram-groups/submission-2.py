class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for string in strs:
            sorteds=''.join(sorted(string))
            dict1[sorteds].append(string)
        return list(dict1.values())


        