# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            val1 = nums[i]
            index2 = val1
            if index2 == len(nums) or val1 == i:
                i+=1
            else:
                val2 = nums[index2]
                nums[index2] = val1
                nums[i] = val2
        
        for i,n in enumerate(nums):
            if i!=n:
                return i
        return len(nums)