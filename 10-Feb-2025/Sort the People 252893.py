# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tupl=[[heights[i],names[i]] for i in range(len(names))]

        for i in range(len(names)):
            swapped=False
            for j in range(1,len(names)-i):
                if tupl[j-1][0]<tupl[j][0]:
                    tupl[j-1],tupl[j]=tupl[j],tupl[j-1]
                    swapped=True
            if not swapped:
                break

        res=[]
        for i in tupl:
            res.append(i[-1])
        return res