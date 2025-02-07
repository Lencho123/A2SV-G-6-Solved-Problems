# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            l=t=0
            r=b=len(matrix)-1
            while l<r and t<b:
                for i in range(r-l):
                    temp=matrix[t+i][r]
                    # swap 1
                    matrix[t+i][r]=matrix[t][l+i]
                    # swap 2
                    temp,matrix[b][r-i]=matrix[b][r-i],temp
                    # swap 3
                    temp,matrix[b-i][l]=matrix[b-i][l],temp
                    # swap 4
                    temp,matrix[t][l+i]=matrix[t][l+i],temp
                l+=1
                t+=1
                r-=1
                b-=1
        for i in range(4):
            rotate(mat)
            if mat==target:
                return True
        return False