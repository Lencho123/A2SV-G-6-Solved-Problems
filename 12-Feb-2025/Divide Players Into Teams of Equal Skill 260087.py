# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target=skill[0]+skill[-1]
        l=0
        r=len(skill)-1
        res=0
        while l<r:
            currSum=skill[l]+skill[r]

            if currSum!=target:
                return -1
            
            res+=skill[l]*skill[r]
            l+=1
            r-=1
        return res

        