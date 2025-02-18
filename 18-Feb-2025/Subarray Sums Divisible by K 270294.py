# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mode=defaultdict(int)
        mode[0]=1

        runsum=0
        res=0

        for num in nums:
            runsum+=num
            mod=runsum%k

            res+=mode[mod]
            mode[mod]+=1
        
        return res