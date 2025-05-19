# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = 1<<len(nums)
        res = [[]]

        for i in range(n):
            subset = []
            for k in range(32):
                if (1 << k) & i !=0:
                    subset.append(nums[k])
            if subset:
                res.append(subset)

        return res