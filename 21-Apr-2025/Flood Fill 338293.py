# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        row = len(image)
        col = len(image[0])

        def inbound(r,c):
            return 0<=r<row and 0<=c<col
        
        def dfs(r,c,color,pixelval):
            visited.add((r,c))
            image[r][c] = color
            for dr,dc in directions:
                _r = r+dr
                _c = c+dc
                if inbound(_r,_c) and image[_r][_c] == pixelval and (_r,_c) not in visited:
                    dfs(_r,_c,color,pixelval)
        
        visited = set()
        dfs(sr,sc,color,image[sr][sc])

        return image