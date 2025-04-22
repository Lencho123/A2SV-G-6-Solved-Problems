# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        row = len(board)
        col = len(board[0])

        def neiMine(r,c):
            count = 0
            for dr,dc in directions:
                _i,_j=r+dr,c+dc
                if inbound(_i,_j) and board[_i][_j] == 'M':
                    count+=1

            return count
        
        def inbound(r,c):
            return 0<=r<row and 0<=c<col

        def bfs(r,c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            elif board[r][c] == 'E' and neiMine(r,c) == 0:
                board[r][c] = 'B'
            elif board[r][c] == 'E' and neiMine(r,c) != 0:
                board[r][c] = str(neiMine(r,c))
                return

            que = deque([(r,c)])
            visited.add((r,c))
            while que:
                i,j = que.popleft()
                for dr,dc in directions:
                    _r,_c = i+dr,j+dc
                    if inbound(_r,_c) and neiMine(_r,_c) == 0 and board[_r][_c] == 'E' and (_r,_c) not in visited:
                        que.append((_r,_c))
                        board[_r][_c] = "B"
                        visited.add((_r,_c))
                    elif inbound(_r,_c) and neiMine(_r,_c) != 0 and board[_r][_c] == 'E':
                        board[_r][_c] = str(neiMine(_r,_c))
        
        i,j=click
        visited = set()
        bfs(i,j)
        return board
                    