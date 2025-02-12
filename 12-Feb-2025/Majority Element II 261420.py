# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        l=len(nums)
        res=[]

        for c in count:
            if count[c]>l/3:
                res.append(c)
        
        return res