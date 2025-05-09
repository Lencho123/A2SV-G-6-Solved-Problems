# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = 0
        directions = [[0,1],[0,-1], [1,0],[-1,0]]
        row,col = len(matrix),len(matrix[0])
        @cache
        def dfs(i,j):
            res = 1

            for dr,dc in directions:
                r = i+dr
                c = j+dc

                if 0<=r<row and 0<=c<col and matrix[i][j]<matrix[r][c]:
                    res = max(res, 1 + dfs(r,c))
            return res

        for i in range(row):
            for j in range(col):
                height = max(height, dfs(i,j))
        
        return height