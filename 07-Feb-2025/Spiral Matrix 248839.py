# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=0
        r=len(matrix[0])-1
        t=0
        b=len(matrix)-1
        res=[]

        while l<=r or t<=b:
        # left to right
            for i in range(r-l+1):
                if l<=r and t<=b:
                    res.append(matrix[t][l+i])
            t+=1

        # top to bottom
            for i in range(b-t+1):
                if l<=r and t<=b:
                    res.append(matrix[t+i][r])
            r-=1

        #  right to left
            for i in range(r-l+1):
                if l<=r and t<=b:
                    res.append(matrix[b][r-i])
            b-=1
        
        # bottom to top
            for i in range(b-t+1):
                if l<=r and t<=b:
                    res.append(matrix[b-i][l])
            l+=1


        return res