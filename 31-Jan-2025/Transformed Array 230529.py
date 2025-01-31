# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[0 for i in range(l)]
        for i in range(l):
            index=i
            if nums[i]==0:
                continue
            elif nums[i]>0:
                index=(i+nums[i])%l
                res[i]=nums[index]
            else:
                n=abs(nums[i])
                index=i-n
                if index<0:
                    index=-1*(abs(index)%l)
                else:
                    index=index%l
                res[i]=nums[index]
        return res