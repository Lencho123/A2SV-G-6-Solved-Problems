# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=defaultdict(int)
        count[0]=1
        runsum=0
        res=0

        for num in nums:
            runsum+=num
            diff=runsum-goal

            if diff in count:
                res+=count[diff]
            count[runsum]+=1
        
        return res