# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        mn_len=len(nums)+1
        runsum=0

        for r in range(len(nums)):
            runsum+=nums[r]

            while runsum >= target:
                mn_len=min(mn_len, r-l+1)
                runsum-=nums[l]
                l+=1
        return mn_len if mn_len != len(nums)+1 else 0