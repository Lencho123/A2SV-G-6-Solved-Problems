# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] ==1:
            return -1
        
        row = len(grid)
        col = len(grid[0])

        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        que = deque([(0,0)])
        grid[0][0] = 1
        
        level = 1
        while que:
            l = len(que)
            isTherePath = False

            for _ in range(l):
                r,c = que.popleft()
                for i,j in directions:
                    _r,_c = r+i,c+j
                    if inbound(_r,_c) and grid[_r][_c] == 0:
                        isTherePath = True
                        que.append((_r,_c))
                        grid[_r][_c] = 1
                        if _r == row-1 and _c == col - 1:
                            return level+1
            
            level+=isTherePath

        if row == 1:
            return 1
        return -1
                        
