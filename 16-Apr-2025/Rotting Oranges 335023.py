# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        row = len(grid)
        col = len(grid[0])
        
        def inbound(r,c):
            return 0<=r<row and 0<=c<col
            
        affected = deque()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    affected.append((i,j))
        
        time = 0

        while affected:
            l = len(affected)
            new_rotten = False

            for n in range(l):
                i,j = affected.popleft()

                for dr,dc in directions:
                    _r = i+dr
                    _c = j+dc
                    if inbound(_r,_c) and grid[_r][_c] == 1:
                        grid[_r][_c] = 2
                        affected.append((_r,_c))
                        new_rotten = True
                        
            time+=new_rotten

        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return time
                        