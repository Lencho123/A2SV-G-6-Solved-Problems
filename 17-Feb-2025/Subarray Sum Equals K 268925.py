# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count=defaultdict(int)
        sum_count[0]=1
        runsum=0
        count=0

        for i in range(len(nums)):
            runsum+=nums[i]
            diff=runsum-k
            count+=sum_count[diff]
            sum_count[runsum]+=1
        return count
