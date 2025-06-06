# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        
        left=0
        res=0
        
        for right in range(len(s)):
            if s[right]=='0':
                res+=right-left
                left+=1
        return res