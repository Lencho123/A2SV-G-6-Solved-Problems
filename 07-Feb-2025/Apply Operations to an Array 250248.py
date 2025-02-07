# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                
        hold=0
        seek=0
        while hold<len(nums) and seek<len(nums):
            while hold<len(nums) and nums[hold]!=0:
                hold+=1
                seek=hold
            
            while seek<len(nums) and nums[seek]==0:
                seek+=1

            if hold<len(nums) and seek<len(nums):
                nums[hold], nums[seek] = nums[seek], nums[hold]


        
        return nums
