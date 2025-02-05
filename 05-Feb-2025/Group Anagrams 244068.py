# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def keyGenerator(s):
            s=list(s)
            s.sort()
            return ''.join(s)
        
        dct=defaultdict(list)
        for s in strs:
            key=keyGenerator(s)
            dct[key].append(s)

        return [v for v in dct.values()]
        