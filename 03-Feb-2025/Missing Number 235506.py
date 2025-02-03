# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=set(nums)
        l=len(num)
        for i in range(l):
            if i not in num:
                return i
        if l not in num:
            return l
        