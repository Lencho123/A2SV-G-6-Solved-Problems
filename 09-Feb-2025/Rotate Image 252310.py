# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=0
        r=len(matrix)-1
        t=0
        b=len(matrix)-1

        while l<r:
            for i in range(r-l):
                # first swap
                temp=matrix[t+i][r]
                matrix[t+i][r]=matrix[t][l+i]

                # second swap
                temp,matrix[b][r-i]=matrix[b][r-i],temp
                # third swap
                temp,matrix[b-i][l]=matrix[b-i][l],temp
                # last swap
                temp,matrix[t][l+i]=matrix[t][l+i],temp

            l+=1
            t+=1
            r-=1
            b-=1
