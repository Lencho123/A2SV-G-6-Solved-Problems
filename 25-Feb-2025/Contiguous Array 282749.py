# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        runsum=0
        dct=defaultdict(int)
        dct[0]=-1
        ln=0

        for i,num in enumerate(nums):
            if num==0:
                runsum-=1
            else:
                runsum+=1
            
            if runsum in dct:
                ln =  max(ln, i-dct[runsum])
            else:
                dct[runsum]=i
        return ln
        