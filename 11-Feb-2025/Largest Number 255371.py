# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=''
        for i in range(len(nums)):
            mx=i
            for j in range(i,len(nums)):
                if str(nums[j])+str(nums[mx])>str(nums[mx])+str(nums[j]):
                    mx=j

            res+=str(nums[mx])
            nums[i],nums[mx]=nums[mx],nums[i]

        zero=True
        for i in res:
            if i!='0':
                zero=False

        return '0' if zero else res