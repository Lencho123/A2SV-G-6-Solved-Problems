# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count=defaultdict(set)
        col_count=defaultdict(set)
        box_count=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                # for row
                if board[i][j] in row_count[i]:
                    return False
                row_count[i].add(board[i][j])
                # for column
                if board[i][j] in col_count[j]:
                    return False
                col_count[j].add(board[i][j])
                # for box
                r=0
                c=0
                if i<=2:
                    r=0
                elif i<=5:
                    r=1
                elif i<=8:
                    r=2
                
                if j<=2:
                    c=0
                elif j<=5:
                    c=1
                elif j<=8:
                    c=2
                key=str(r)+str(c)
                if board[i][j] in box_count[key]:
                    return False
                box_count[key].add(board[i][j])

        return True
