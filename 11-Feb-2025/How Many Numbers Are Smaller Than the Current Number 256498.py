# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:  
        copy=nums.copy()
        nums.sort()
        count=defaultdict(int)
        d=defaultdict(int)
        
        l=len(nums)
        res=[]

        for i in range(l):
            d[nums[i]]=i-count[nums[i]]
            count[nums[i]]+=1
        
        for i in copy:
            res.append(d[i])

        return res