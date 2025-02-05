# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=0
        for i in nums:
            if i%2==0:
                total+=i
        
        res=[]
        for val, index in queries:
            if abs(nums[index])%2!=0:
                nums[index]+=val
                if abs(nums[index])%2==0:
                    total+=nums[index]
            else:
                total-=nums[index] #delete prev contribution
                nums[index]+=val
                if abs(nums[index])%2==0:
                    total+=nums[index]
            res.append(total)
        return res