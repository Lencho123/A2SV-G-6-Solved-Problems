# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            val1 = nums[i]
            index2 = val1 - 1
            val2 = nums[index2]

            if nums[i] == i+1 or val1 == val2:
                i+=1
                if val1 == val2:
                    duplicate = val1
            else:
                nums[i] = val2
                nums[index2] =val1

        for i,n in enumerate(nums):
            if n != i+1:
                return [n,i+1]
