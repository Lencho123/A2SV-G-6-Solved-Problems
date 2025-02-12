# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)

        pair=0
        leftover=0
        for n in count:
            pair+=count[n]//2
            leftover+=count[n]%2
        
        return [pair,leftover]
