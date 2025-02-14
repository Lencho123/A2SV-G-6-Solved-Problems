# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costArr=[]
        for i in range(len(s)):
            cost=abs(ord(s[i])-ord(t[i]))
            costArr.append(cost)

        left=0
        res=0
        runsum=0

        for right in range(len(s)):
            runsum+=costArr[right]
            while runsum > maxCost:
                runsum-=costArr[left]
                left+=1
            
            res = max(res, right - left + 1)
        
        return res