# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for i in count:
            if count[i]>=2:
                res.append(i)
            if len(res)==2:
                return res
        
        return res