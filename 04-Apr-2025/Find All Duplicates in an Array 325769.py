# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            val1 = nums[i]
            index2 = val1 - 1
            val2 = nums[index2]

            if val1 == i+1 or val1 == 0:
                i+=1
            elif val1 == val2:
                res.append(val1)
                nums[i] = 0
                nums[index2] = 0
            else:
                nums[i] = val2
                nums[index2] = val1
        return res