# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runsum=0
        dct=defaultdict(int)
        dct[0]=-1

        for right in range(len(nums)):
            runsum+=nums[right]
            mod=runsum%k
            if mod in dct and right-dct[mod]>=2:
                return True
            elif mod not in dct:
                dct[mod]=right

        return False