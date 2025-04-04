# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            val1 = nums[i]
            index2 = nums[i]-1
            val2 = nums[index2]

            if val1 == i+1 or val2 == index2+1:
                i+=1
            else:
                nums[i] = val2
                nums[index2] = val1
        
        res = []
        for i, n in enumerate(nums):
            if n!=i+1:
                res.append(i+1)
        return res