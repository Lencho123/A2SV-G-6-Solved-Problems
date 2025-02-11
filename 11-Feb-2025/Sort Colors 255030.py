# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # collect 0's to left
        l=0
        r=len(nums)-1
        while l<r:
            while l<r and nums[l]==0:
                l+=1
            while l<r and nums[r]!=0:
                r-=1
            # swap
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        
        # collect 1's to middle
        l=0
        r=len(nums)-1
        # move left to first non zero
        while l<r and nums[l]==0:
            l+=1
        
        while l<r:
            while l<r and nums[l]==1:
                l+=1
            while l<r and nums[r]==2:
                r-=1
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
