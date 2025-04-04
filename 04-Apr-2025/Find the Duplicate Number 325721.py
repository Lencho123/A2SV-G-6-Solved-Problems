# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            val1 = nums[i]
            index2 = val1-1
            val2 = nums[index2]
            
            if val1 == i+1:
                i+=1
            elif val1 == val2:
                return val1
            else:
                nums[i] = val2
                nums[index2] = val1