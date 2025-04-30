# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n,m = len(grid),len(grid[0])
        can_arr = []
        res = 0
        for i,row in enumerate(grid):
            sorted_row = sorted(row)
            sorted_row.reverse()
            can_arr+=sorted_row[:limits[i]]
        
        can_arr.sort(reverse = True)
        return sum(can_arr[:k])