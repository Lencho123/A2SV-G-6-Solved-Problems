# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left=0
        mid=0
        large_win=defaultdict(int)
        small_win=defaultdict(int)
        res=0

        for right in range(len(nums)):
            large_win[nums[right]]+=1
            small_win[nums[right]]+=1

            # check validity of both window
            while len(large_win)>k:
                large_win[nums[left]]-=1
                if large_win[nums[left]]==0:
                    large_win.pop(nums[left])
                left+=1

            while len(small_win)>k:
                small_win[nums[mid]]-=1
                if small_win[nums[mid]]==0:
                    small_win.pop(nums[mid])
                mid+=1
            
            # shrink small window to find smallest valid window
            while small_win[nums[mid]]>1:
                small_win[nums[mid]]-=1
                mid+=1
            
            # update result if windows are valid
            if len(large_win)==k:
                res+=mid-left+1
        
        return res
