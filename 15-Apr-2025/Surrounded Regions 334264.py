# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col

        def markWith(r,c, char,cell):
            if char == 'U':
                board[r][c] = 'U'
            elif char == 'X':
                board[r][c] = 'X'
            else:
                board[r][c] = 'O'
            for dr,dc in directions:
                _r = dr + r
                _c = dc + c
                if inbound(_r,_c) and board[_r][_c] == cell:
                    markWith(_r,_c, char, cell)
        

        for i in range(row):
            for j in range(col):
                if (i == 0 or j == 0 or i == row-1 or j == col - 1) and board[i][j] == 'O':
                    markWith(i,j, 'U','O')

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    markWith(i,j, 'X', 'O')
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'U':
                    markWith(i,j, 'O', 'U')

        
        


