# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        slot_count = [0 for i in range(32)]

        def add(n):
            for i in range(n.bit_length()):
                if n&(1<<i) != 0:
                    slot_count[i]+=1
        def remove(n):
            for i in range(n.bit_length()):
                if n&(1<<i) != 0:
                    slot_count[i]-=1

        l=0
        res = 1
        for r in range(len(nums)):
            add(nums[r])
            while max(slot_count)>1:
                remove(nums[l])
                l+=1
            res = max(res,r-l+1)
    
        return res