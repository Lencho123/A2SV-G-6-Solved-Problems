# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum=0
        runsum=0
        max_sum=nums[0]

        for num in nums:
            runsum+=num
            max_sum=max(max_sum, runsum-min_sum)
            min_sum=min(min_sum, runsum)
        
        return max_sum