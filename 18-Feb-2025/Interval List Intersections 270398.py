# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1,p2=0,0

        res=[]
        while p1 < len(firstList) and p2 < len(secondList):
            if secondList[p2][0] <= firstList[p1][0] <= secondList[p2][1] or firstList[p1][0] <= secondList[p2][0] <= firstList[p1][1]:
                res.append([max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1], secondList[p2][1])])
            
            if firstList[p1][1]<secondList[p2][1]:
                p1+=1
            else:
                p2+=1
        
        return res