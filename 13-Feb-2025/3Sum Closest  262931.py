# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff=float('inf')
        ans=0
        lenth=len(nums)

        for i in range(lenth-2):
            l=i+1
            r=lenth-1

            while l<r:
                runsum=nums[i]+nums[l]+nums[r]
                diff=abs(target-runsum)
                print(runsum)
                
                if min_diff > diff:
                    ans=runsum
                    min_diff=diff
                
                if runsum > target:
                    r-=1
                else:
                    l+=1
        return ans