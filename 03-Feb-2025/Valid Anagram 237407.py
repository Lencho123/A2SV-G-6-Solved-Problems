# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc=Counter(s)
        tc=Counter(t)

        if len(sc)!=len(tc):
            return False
        for i in sc:
            if sc[i]!=tc[i]:
                return False
        
        return True
        