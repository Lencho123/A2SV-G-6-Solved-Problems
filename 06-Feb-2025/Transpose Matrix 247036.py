# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        transpose=[[0 for _ in range(r)] for p in range(c)]

        for i in range(r):
            for j in range(c):
                transpose[j][i]=matrix[i][j]
        
        return transpose