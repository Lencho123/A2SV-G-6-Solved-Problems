# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(smallLargeSum):
            split = 1
            runsum = 0
            for n in nums:
                runsum+=n
                if runsum > smallLargeSum:
                    split+=1
                    runsum = n
            return split <= k

        l = max(nums)
        r = sum(nums)
        res = 0
        while l <= r:
            m = (l+r)//2
            if canSplit(m):
                res = m
                r = m-1
            else:
                l = m+1
        
        return res