# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # use index dictionary with marking.
        res=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                res.append(abs(nums[i]))
            nums[index]*=-1
        return res