# Problem: Count complete subarrays in an array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k=len(set(nums))
        left=0
        mid=0

        small_window=defaultdict(int)
        large_window=defaultdict(int)
        res=0

        for right in range(len(nums)):
            small_window[nums[right]]+=1
            large_window[nums[right]]+=1

            # check validity of both window
            while len(large_window) > k:
                large_window[nums[left]]-=1
                if large_window[nums[left]]==0:
                    large_window.pop(nums[left])
                left+=1

            while len(small_window) > k:
                small_window[nums[mid]]-=1
                if small_window[nums[mid]]==0:
                    small_window.pop(nums[mid])
                mid+=1

            # find the smallest possible window up to right pointer
            while small_window[nums[mid]] > 1:
                small_window[nums[mid]]-=1
                mid+=1
            
            # accomulate result if windows are valid
            if len(large_window)==k:
                res+=mid-left+1
        
        return res
            