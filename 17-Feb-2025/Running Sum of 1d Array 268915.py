# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        runsum=0
        for i in nums:
            runsum+=i
            res.append(runsum)
        return res
        