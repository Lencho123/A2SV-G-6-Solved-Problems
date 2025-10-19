# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(sm):
            if sm == target:
                return 1
            if sm > target:
                return 0
            
            temp = 0
            if sm not in dp:
                for i in range(len(nums)):
                    temp+=dfs(sm+nums[i])
                dp[sm] = temp

            return dp[sm]

        return dfs(0)