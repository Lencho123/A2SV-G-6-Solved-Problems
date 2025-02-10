# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dct=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                dct[i+j].append(mat[i][j])
        
        res=[]
        for i in dct:
            if i%2==0:
                dct[i].reverse()
            res+=dct[i]
        
        return res