# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l=0
        r=len(s1)-1
        count1=Counter(s1)
        count2=Counter(s2[:r])

        for i in range(r,len(s2)):
            count2[s2[i]]+=1

            if count2==count1:
                return True
            
            count2[s2[l]]-=1
            l+=1

        return False