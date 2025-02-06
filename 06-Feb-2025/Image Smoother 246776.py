# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row=len(img)
        col=len(img[0])
        res=[[0 for c in range(col)] for r in range(row)]

        for i in range(row):
            for j in range(col):
                top,bottom,left,right,topL,topR,bottomL,bottomR=0,0,0,0,0,0,0,0
                num=1
                if i>0:
                    top=img[i-1][j]
                    num+=1
                if i<row-1:
                    bottom=img[i+1][j]
                    num+=1
                if j>0:
                    left=img[i][j-1]
                    num+=1
                if j<col-1:
                    right=img[i][j+1]
                    num+=1

                if i>0 and j>0:
                    topL=img[i-1][j-1]
                    num+=1
                if i<row-1 and j<col-1:
                    bottomR=img[i+1][j+1]
                    num+=1
                if i>0 and j<col-1:
                    topR=img[i-1][j+1]
                    num+=1
                if i<row-1 and j>0:
                    bottomL=img[i+1][j-1]
                    num+=1
                
                average=(top+bottom+left+right+topL+topR+bottomR+bottomL+img[i][j])//num
                res[i][j]=average

        return res