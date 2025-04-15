# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def inbound(r,c):
            return 0<=r<row and 0<=c<col

        def dfs(r,c):
            nonlocal area
            area+=1
            grid[r][c]=0
            for dr,dc in directions:
                _r = r+dr
                _c = c+dc
                if inbound(_r,_c) and grid[_r][_c] == 1:
                    dfs(_r,_c)
        
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    res = max(area,res)
        
        
        return res


