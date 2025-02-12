# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r=len(people)-1

        l=0
        pair=0
        while l<r:
            if people[l]+people[r]<=limit:
                pair+=1
                l+=1
            r-=1
            
        return len(people)-pair

