# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length=len(nums)
        pre=[0 for i in range(length+1)]

        for start,end in requests:
            pre[start]+=1
            pre[end+1]-=1

        for i in range(1,length+1):
            pre[i]=pre[i]+pre[i-1]
        
        pre=pre[:-1]
        nums.sort()
        pre.sort()

        max_sum=0
        for i in range(length):
            max_sum+=nums[i]*pre[i]

        return max_sum%(10**9 + 7)