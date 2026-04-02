class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        # for string in strs:
        #     sorteds=''.join(sorted(string))
        #     dict1[sorteds].append(string)
        # return list(dict1.values())

        for s in strs:
            count=[0]*26
            for ch in s:
                count[ord(ch)-ord('a')] +=1
            dict1[tuple(count)].append(s)
        return list(dict1.values())
                



        