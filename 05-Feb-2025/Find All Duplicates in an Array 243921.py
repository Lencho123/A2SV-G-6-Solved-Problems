# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()

        track=0
        left=0
        right=1

        while right<len(nums):
            if nums[right]==nums[left]:
                nums[track]=nums[left]
                track+=1
            while right<len(nums) and nums[left]==nums[right]:
                right+=1
            
            left=right
            right+=1
        return nums[:track]
