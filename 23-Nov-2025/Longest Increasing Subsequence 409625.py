# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # BOTTOM UP APPROACH
        n = len(nums)
        DP = [1]*n
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if nums[i] < nums[j]:
                    DP[i] = max(DP[i], 1+DP[j])
        return max(DP)
        
        # # ===TOP DOWN SOLUTION===
        # dp = {}
        # def dfs(ind):

        #     if ind in dp:
        #         return dp[ind]
            
        #     temp = 1
        #     for i in range(ind,len(nums)):
        #         if nums[ind] < nums[i]:
        #             temp = max(temp, 1+dfs(i))
        #     dp[ind] = temp
        #     return dp[ind]
            
        # return max(dfs(i) for i in range(len(nums)))