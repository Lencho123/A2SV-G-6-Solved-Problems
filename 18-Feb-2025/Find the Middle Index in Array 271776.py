# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre=[0 for i in range(len(nums))]
        post=[0 for i in range(len(nums))]

        for i in range(1,len(nums)):
            pre[i]=pre[i-1]+nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            post[i]=post[i+1]+nums[i+1]
        
        for i in range(len(nums)):
            if post[i]==pre[i]:
                return i
        return -1