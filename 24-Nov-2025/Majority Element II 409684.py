# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = 1
        pre_num = nums[0]
        res = [] 
        nums.sort()
        for i in range(1,n):
            if pre_num == nums[i]:
                count+=1
            else:
                if count > n/3:
                    res.append(pre_num)
                count = 1
                pre_num = nums[i]
        if count > n/3:
            res.append(pre_num)
        return res