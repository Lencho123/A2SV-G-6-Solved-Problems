# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        zeros=0
        mx=0

        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1

            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            mx=max(mx, right-left+1)

        return mx