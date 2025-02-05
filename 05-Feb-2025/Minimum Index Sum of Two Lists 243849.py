# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c1=defaultdict(int)
        c2=defaultdict(int)

        for i, s in enumerate(list1):
            if s in c1:
                continue
            c1[s]=i
        
        for i, s in enumerate(list2):
            if s in c2:
                continue
            c2[s]=i

        cIndex=defaultdict(list)
        for string in c1:
            if string in c2:
                index=c1[string]+c2[string]
                cIndex[index].append(string)
        
        minIndex=min(cIndex.keys())
        
        return cIndex[minIndex]