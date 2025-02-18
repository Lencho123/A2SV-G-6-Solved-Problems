# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.pre=[[0 for _ in range(len(self.matrix[0])+1)] for _ in range(len(self.matrix)+1)]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.pre[i+1][j+1]=self.pre[i+1][j] + self.pre[i][j+1] - self.pre[i][j] + self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sm=self.pre[row2+1][col2+1] - self.pre[row2+1][col1] - self.pre[row1][col2+1] + self.pre[row1][col1]
        return sm

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)