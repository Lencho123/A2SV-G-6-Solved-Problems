# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mxsum=sum(nums[:k])
        window=mxsum
        l=0
        for r in range(k, len(nums)):
            window = window-nums[l]+nums[r]
            mxsum=max(window, mxsum)
            l+=1
        return mxsum/k

        