# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_n=0
        max_n=0

        runsum=0
        for num in nums:
            runsum+=num
            min_n=min(min_n, runsum)
            max_n=max(max_n, runsum)

        return abs(max_n-min_n)